#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.header    import Header
from email.mime.text import MIMEText
from getpass import getpass
from smtplib import SMTP_SSL

# provide credentials
login = "snippythelobster@yahoo.com"
password = "beautifulsoup"

# create message
msg = MIMEText('message body…', 'plain', 'utf-8')
msg['Subject'] = Header('subject…', 'utf-8')
msg['From'] = login
msg['To'] = ', '.join([login, ])

# send it   
s = SMTP_SSL("smtp.mail.yahoo.com", timeout=10) #NOTE: no server cert. check
s.set_debuglevel(0)
try:
	s.connect()
	s.login(login, password)
	s.sendmail(msg['From'], msg['To'], msg.as_string())
finally:
    s.quit()