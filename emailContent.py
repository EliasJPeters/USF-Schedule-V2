import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
from email.mime.text import MIMEText
import ssl

email_sender = "usfclassbot@gmail.com"
email_password = "tgtnxufmyurgpxxa"

def initialEmail(crn, email, courseNumber):
    subject = ("Hello! You've chosen to be notified of seat openings for the class with the CRN of: " + crn)
    body = ("You will be emailed a notification when an open seat is detected for: " + courseNumber + "\n\nThanks for using this program!\n" + 
    "This project was created by Elias Peters. You can get more information from the github here: https://github.com/EliasJPeters/USF-Schedule-V2")
    
    email_receiver = email
    msg = EmailMessage()
    msg["From"] = email_sender
    msg["To"] = email_receiver
    msg["Subject"] = subject
    msg.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, msg.as_string())