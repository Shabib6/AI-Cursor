# AI Cursor Automation Tool

This project is an AI-powered desktop automation tool that lets you control your computer with natural language commands. It connects with Command Prompt, Gmail, and WhatsApp, allowing you to perform tasks like sending emails or messages by simply telling the system what to do.

## ✨ Features

- Control your system using natural language.
- Get system info in plain English, like you’re talking to your PC.
- Send emails via Gmail through an interactive prompt.
- Send WhatsApp messages by automating WhatsApp Web.
- Uses OCR with pytesseract to detect UI elements.

## ⚙️ Tech Stack

- **Python**
- **PyAutoGUI** for cursor automation
- **OpenCV & pytesseract** for screen OCR
- **webbrowser** module for opening apps like WhatsApp Web
- **time** module for delays

## 🚀 Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the main script:
    ```bash
    python main.py
    ```

4. Follow the prompts to send messages or perform tasks.

## 📝 Notes

- Make sure you are logged into WhatsApp Web before trying to send messages.
- Adjust sleep delays (`time.sleep`) if your internet or system speed varies.

## 📄 License

This project is open source under the MIT License. See [LICENSE](LICENSE) for details.
