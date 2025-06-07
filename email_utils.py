import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_email_with_attachment(to_email, subject, body, attachment_path):
    gmail_user = os.getenv("GMAIL_USER")  # should be star@soulblueprint.co.uk
    gmail_password = os.getenv("GMAIL_PASSWORD")  # your Gmail app password

    if not gmail_user or not gmail_password:
        raise ValueError("Missing Gmail credentials in .env")

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = f"Soul Aligned <{gmail_user}>"
    msg['To'] = to_email
    msg.set_content(body)

    # Attach PDF
    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)
        msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

    # Send email using TLS (port 587)
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(gmail_user, gmail_password)
        smtp.send_message(msg)
