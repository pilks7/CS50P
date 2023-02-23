import smtplib, ssl, email #for email
import csv
import time
from datetime import date
import sys

class Contractor:
	def __init__(self):
		...

def main():
	...


def send_email():

	port = 465  # For SSL
	email = ''######################
	password = ''###########SECURE PASSWORD STORING METHOD??

	# Create a secure SSL context
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	    server.login(email, password)
	    # TODO: Send email here
	    email_template = '''


	    '''
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
password = input("Type your password and press enter:")

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = ''  # FILENAME HERE - - - In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)





if __name__ == '__main__':
	main()


#	key=API_KEY 
#	'AIzaSyAOvr6JZZeXDnocLMKFWzImIu39wLlWfD8'