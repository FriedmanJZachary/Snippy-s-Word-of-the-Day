#!/usr/bin/env python3

#In honor of 'Dave' Do Hyung Kwon, may the glory of his saintly presence remain an eternal blessing
#In honor of Allen Ravitsky, for every Saint needs a Satan

from bs4 import BeautifulSoup
import requests
import smtplib, ssl
from email.mime.text import MIMEText as text

#OLD LINK _______________________________________________________________________

link = "https://www.nytimes.com/column/learning-word-of-the-day"
data = requests.get(link).text
soup = BeautifulSoup(data, features="html.parser")
mydivs = soup.findAll("div", {"class": "css-1l4spti"})
 
for a in mydivs[0].find_all('a', href=True):
    ext = a['href']

#NEW LINK _______________________________________________________________________

newlink = "https://www.nytimes.com/" + ext
newdata = requests.get(newlink).text
newsoup = BeautifulSoup(newdata, features="html.parser")

div_container = newsoup.find('div', class_='css-1fanzo5 StoryBodyCompanionColumn')  

msg = ""

for tag in div_container.find_all('h2'):
    msg = msg + tag.text

headLine = msg.split("\\")
word = headLine[0]

msg = msg + "\n"

for tag in div_container.find_all('p'):
	if tag.text[0].isdigit() or ":" in tag.text[0:10]:
		msg = msg + "\n" + tag.text

msg = msg + "\n"

#import pdb; pdb.set_trace()


#EMAIL _________________________________________________________________________

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "snippythelobster@gmail.com"  # Enter your address
receiver_email = "friedmanjzachary@gmail.com"  # Enter receiver address
password = "beautifulsoup"
message = msg

context = ssl.create_default_context()
with smtplib.SMTP('localhost', port) as server:
	server.login(sender_email, password)

	m = text(message)
	m['Subject'] = "Word of the Day | " + word
	m['From'] = sender_email
	m['To'] = receiver_email
	server.sendmail(sender_email, receiver_email, m.as_string())



