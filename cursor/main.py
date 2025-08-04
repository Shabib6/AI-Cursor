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

load_dotenv()
client = os.getenv("OPENAI_API_KEY")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# C:\Program Files\Tesseract-OCR

def parse_prompt_to_intent(prompt):
    system_prompt = """
    You are a command interpreter AI. Convert the user's natural language request into a JSON plan for automation.

    Example:
    User: Compose a mail to syedshabib6@gmail.com enquiring about the stock market.
    Output:
    for gmail:
    {
    "app": "gmail",
    "action": "compose",
    "to": "syedshabib6@gmail.com",
    "subject": "Stock Market Enquiry",
    "body": "Dear Syed, I hope you're doing well. I would like to enquire about the recent stock market changes in the firm."
    }
    for whatsapp:
    {
    "app": "whatsapp",
    "action": "send_message",
    "to": "Thoufiq Ahamed",
    "message": "Hey Thoufiq, please be ready with the report for the meeting at 10:30 pm tonight!"
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

if __name__ == "__main__":
    user_prompt = input("What is your request?  ")
    parsed = parse_prompt_to_intent(user_prompt)
    print("Parsed Intent:", parsed)
    parsed = json.loads(parsed)
    if parsed["app"] == "gmail":
        gmail(parsed)
    elif parsed["app"] == "whatsapp":
        whatsapp(parsed)
    else:
        print("Unsupported app.")