import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv

load_dotenv()
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = os.getenv("EMAIL_HOST_USER")
password = os.getenv("EMAIL_HOST_PASSWORD")
path_to_file = 'python.txt'

receiver_email = 'nika@mziuri.ge'

message = MIMEMultipart() 
message['Subject'] = 'tatotask21'
message['From'] = sender_email
message['To'] = receiver_email

message.attach(MIMEText("Hello Nika, this is a test mail with an attachment!", 'plain'))

with open(path_to_file, 'rb') as file:
    part = MIMEApplication(file.read(), Name='python.txt')
    part['Content-Disposition'] = 'attachment; filename="python.txt"'
    message.attach(part)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")