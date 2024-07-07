import smtplib
import ssl
from email.message import EmailMessage

subject = input("Enter the subject of the email: ")
body = input("Enter the body of the email: ")
sender_email = input("Enter your email: ")
receiver_email = input("Enter the receiver's email: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.zoho.eu", 465, context=context) as server:
    server.login(sender_email, input("Enter your password: "))
    server.send_message(message)
