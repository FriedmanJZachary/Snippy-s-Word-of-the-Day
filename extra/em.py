#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import requests
import smtplib, ssl

sender = "snippythelobster@gmail.com"
receivers = ["friedmanjzachary@gmail.com"]

port = 465
msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

with smtplib.SMTP('localhost', port) as server:
	server.connect("smtp.gmail.com", 465)
	server.login('snippythelobster@gmail.com', 'beautifulsoup')
	server.sendmail(sender, receivers, msg.as_string())

# msg = "MESSAGE BODY"
# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "snippythelobster@gmail.com"  # Enter your address
# receiver_email = "friedmanjzachary@gmail.com"  # Enter receiver address
# password = "beautifulsoup"
# message = "TEST"


# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)