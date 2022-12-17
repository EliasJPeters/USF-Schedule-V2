import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
from email.mime.text import MIMEText
import ssl

recipient = ""

email_sender = "usfclassbot@gmail.com"
email_password = "tgtnxufmyurgpxxa"
email_receiver = recipient

subject = "Test message subject"
body = """
Test message body
with multiple lines
to test the newline
"""

msg = EmailMessage()
msg["From"] = email_sender
msg["To"] = email_receiver
msg["Subject"] = subject
msg.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, msg.as_string())