import os
import openai
from dotenv import load_dotenv
import pyautogui
import time 
import webbrowser
import pyperclip
import json
import pytesseract
import cv2
import subprocess

load_dotenv()
client = os.getenv("OPENAI_API_KEY")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# C:\Program Files\Tesseract-OCR

def parse_prompt_to_intent(prompt):
    system_prompt = """
    You are a command interpreter AI. 
    Convert the user's natural language request into a JSON object ONLY. 
    Do not include any text outside JSON. 
    Output must be strictly valid JSON.

    Examples:

    User: Compose a mail to syedshabib6@gmail.com enquiring about the stock market.
    Output:
    {
    "app": "gmail",
    "action": "compose",
    "to": "syedshabib6@gmail.com",
    "subject": "Stock Market Enquiry",
    "body": "Dear Syed, I hope you're doing well. I would like to enquire about the recent stock market changes in the firm."
    }

    User: Send a WhatsApp message to Thoufiq Ahamed to be ready with the report for the meeting at 10:30 pm tonight.
    Output:
    {
    "app": "whatsapp",
    "action": "send_message",
    "to": "Thoufiq Ahamed",
    "message": "Hey Thoufiq, please be ready with the report for the meeting at 10:30 pm tonight!"
    }

    User: Show me all the files in the Documents folder.
    Output:
    {
    "app": "os",
    "action": "run_command",
    "command": "dir C:\\Users\\<username>\\Documents"
    }

    User: Check my current IP address.
    Output:
    {
    "app": "os",
    "action": "run_command",
    "command": "ipconfig"
    }
    """


    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [ 
            {"role": "system" , "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

def gmail(text):
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=CllgCJTLpRFSlsgLHmDPxXxBNhvZVMZWRczfRFzJkrvCKNSJqnMjlNCKplGcVPwwdMtzdsVcxdV")
    time.sleep(10)
    screenshot = pyautogui.screenshot()
    screenshot.save("screen.png")
    img = cv2.imread("screen.png")
    boxes = pytesseract.image_to_data(img)
    compose_cord = send_cord = None 
    for i,line in enumerate(boxes.splitlines()):
        if i == 0:
            continue
        parts = line.split()
        if len(parts) == 12:
            x,y,w,h,text = int(parts[6]), int(parts[7]), int(parts[8]), int(parts[9]), parts[11]
            if text.lower() == "compose":                                                                   #ONLY FOR COMPOSE BUTTON
                print(f"Found 'compose' at ({x}, {y})")
                compose_cord = (x + w//2, y + h//2)
                pyautogui.moveTo(compose_cord[0], compose_cord[1], duration=2)
                pyautogui.click()
                time.sleep(2)
                pyperclip.copy(parsed["to"])
                pyautogui.hotkey("ctrl","v")
                pyautogui.press("tab")
                pyperclip.copy(parsed["subject"])
                pyautogui.hotkey("ctrl","v")
                pyautogui.press("tab")
                
                pyperclip.copy(parsed["body"])
                pyautogui.hotkey("ctrl","v")

                pyautogui.hotkey("ctrl","enter")
                time.sleep(2)
            elif text.lower() == "send":
                send_cord = (x + w//2, y + h//2)
                print(f"Found 'send' at ({x}, {y})")    
    if send_cord:
        time.sleep(10)
        pyautogui.moveTo(send_cord[0] , send_cord[1], duration=1)
        pyautogui.click()
    
def whatsapp(text):
    webbrowser.open("https://web.whatsapp.com/")
    time.sleep(20)
    screenshot = pyautogui.screenshot()
    screenshot.save("whats_screen.png")
    #img = cv2.imread("whats_screen.png")

    pyautogui.moveTo(277,252, duration=2)
    pyautogui.click()
    pyautogui.typewrite(parsed["to"])
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)

    region = (100,100, 800, 600)  
    contact_img = pyautogui.screenshot(region=region)
    contact_img.save("contact_check.png")

    text_detected = pytesseract.image_to_string(contact_img)
    for i,line in enumerate(text_detected.splitlines()):
        if parsed["to"].lower() in line.lower():
            print(f"Found contact '{parsed['to']}' in the screenshot.")
            #contact_cord = pyautogui.locateCenterOnScreen("contact_check.png", confidence=0.8)
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.typewrite(parsed["message"])
            pyautogui.press("enter")
            break


def run_command(text):
    command = text["command"]

    # safety check
    dangerous = ["rm -rf", "del *", "shutdown", "format"]
    if any(cmd in command.lower() for cmd in dangerous):
        return "❌ Command looks dangerous, not executing."

    result = subprocess.run(command,shell=True, capture_output=True, text=True)
    output = result.stdout.strip()
    error = result.stderr.strip()
    returncode  = result.returncode

    system_prompt2 = """
    You are a System Resource Interpreter Assistant.
    You will receive the following information:
    - The output of a system command (like free -m, df -h, top, tasklist, ping, etc.)
    - Any error messages (if present),
    - The return code.

    Your tasks are:
    1. First, check if the command executed successfully:
    - If NOT successful: explain the error in simple terms and suggest possible fixes.
    - If successful: move to step 2.

    2. Identify what resource or aspect the command relates to (e.g., RAM, CPU, Disk, Network, Processes, etc.).

    3. Summarize the results in clear, human-friendly language. Example style:
    - "CPU is at 75% usage, which is slightly high."
    - "Disk usage is 92% full on drive /, system may slow down."
    - "Network latency is stable at ~20ms, no issues detected."

    4. Provide practical, actionable advice for optimization or troubleshooting:
    - For CPU: "Close unnecessary heavy apps", "Check for background processes."
    - For Disk: "Remove unused files", "Consider upgrading storage."
    - For Network: "Check Wi-Fi strength", "Restart router if latency spikes."
    - For Errors: "Re-run with sudo", "Verify the path is correct."

    5. Add extra insights when useful:
    - Compare usage to normal/healthy ranges.
    - Mention potential risks if values are abnormal.
    - Suggest follow-up commands for deeper analysis.

    6. Keep explanations supportive, concise, and beginner-friendly.

    7. End with suggested next steps (if any).
    """


    response2 = openai.chat.completions.create(
        model = "gpt-4o",
        messages= [
            {"role": "system", "content": system_prompt2},
            {"role": "user", "content": f"Output: {output}\nError: {error}\nReturn Code: {returncode}"}
        ]
    )
    return response2.choices[0].message.content.strip()



if __name__ == "__main__":
    user_prompt = input("What is your request?  ")
    parsed = parse_prompt_to_intent(user_prompt)
    print("Parsed Intent:", parsed)
    parsed = json.loads(parsed)
    if parsed["app"] == "gmail":
        gmail(parsed)
    elif parsed["app"] == "whatsapp":
        whatsapp(parsed)
    elif parsed["app"] == "os":
        os_says = run_command(parsed)
        print("Command Output:", os_says)
    else:
        print("Unsupported app.")