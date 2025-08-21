# AI Cursor

AI Cursor is a Python-powered desktop automation tool that uses OCR and natural language processing to control your screen intelligently. It reads visible text, locates UI elements like buttons, and performs clicks or typing based on your commands—just like a human would, without needing HTML or DOM access.

## Features

- **Natural Language Control**: Control your system using plain English commands
- **System Information**: Get system info in conversational language, like talking to your PC
- **Gmail Integration**: Send emails through an interactive prompt interface
- **WhatsApp Automation**: Send WhatsApp messages by automating WhatsApp Web
- **OCR-Powered UI Detection**: Uses Tesseract OCR to detect and interact with UI elements
- **Cross-Platform**: Works on any desktop environment with visual elements

## Technologies Used

- **Python** - Core programming language
- **PyAutoGUI** - Cursor automation and screen control
- **OpenCV** - Image processing and computer vision
- **pytesseract** - OCR (Optical Character Recognition) for text detection
- **webbrowser** - Opening web applications like WhatsApp Web
- **time** - Managing delays and timing

## Prerequisites

Before running AI Cursor, make sure you have:

- Python 3.6 or higher installed
- Tesseract OCR installed on your system
- A webcam or screen capture capability
- Active internet connection for web-based features

### Installing Tesseract OCR

**Windows:**
```bash
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
# Or using chocolatey:
choco install tesseract
```

**macOS:**
```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install tesseract-ocr
```

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shabib6/AI-Cursor.git
   cd AI-Cursor
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the main script:**
   ```bash
   python main.py
   ```

## 📱 Usage

### Basic Commands
Once you run the script, you can:

1. **System Control**: Use natural language to describe what you want to do
2. **Email Sending**: Follow prompts to send emails via Gmail
3. **WhatsApp Messages**: Automate message sending through WhatsApp Web
4. **UI Interaction**: Click buttons, fill forms, and navigate interfaces

### Example Commands
```
"Click on the submit button"
"Type 'Hello World' in the text field"
"Open Gmail and send an email"
"Send a WhatsApp message to John"
```

## ⚙️ Configuration

### Important Setup Notes

- **WhatsApp Web**: Make sure you're logged into WhatsApp Web before attempting to send messages
- **Sleep Delays**: Adjust `time.sleep()` values in the code if your internet or system speed varies
- **Screen Resolution**: The tool adapts to different screen resolutions automatically
- **OCR Accuracy**: Ensure good lighting and clear text for better OCR recognition

### Performance Optimization

- Close unnecessary applications to improve OCR accuracy
- Use high contrast themes for better text detection
- Ensure stable internet connection for web-based features

## 🔧 Troubleshooting

### Common Issues

1. **OCR Not Working**: 
   - Verify Tesseract is properly installed
   - Check if text is clearly visible on screen
   - Adjust screen brightness and contrast

2. **WhatsApp Messages Failing**:
   - Ensure you're logged into WhatsApp Web
   - Check internet connection
   - Verify WhatsApp Web is accessible in your browser

3. **Gmail Integration Issues**:
   - Check Gmail accessibility settings
   - Verify internet connection
   - Ensure you're logged into Gmail

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🚨 Disclaimer

This tool is designed for legitimate automation purposes. Users are responsible for:
- Complying with terms of service of applications they automate
- Respecting privacy and security guidelines
- Using the tool ethically and legally

## 🆘 Support

If you encounter issues or have questions:

1. Check the [Issues](https://github.com/Shabib6/AI-Cursor/issues) section
2. Create a new issue with detailed information
3. Provide your system specifications and error messages

## 🎯 Roadmap

- [ ] Add more natural language processing capabilities
- [ ] Implement voice command support
- [ ] Add support for more applications
- [ ] Improve OCR accuracy and speed
- [ ] Create GUI interface
- [ ] Add keyboard shortcut support

---

**Developed By [Shabib6](https://www.linkedin.com/in/syed-shabib-ahamed-b673b0225/)**

*Star ⭐ this repository if you find it helpful!*