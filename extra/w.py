#!/usr/bin/env python3

#In honor of 'Dave' Do Hyung Kwon, may the glory of his saintly presence remain an eternal blessing
#In honor of Allen Ravitsky, for every Saint needs a Satan

from bs4 import BeautifulSoup
import requests
import smtplib, ssl
from email.mime.text import MIMEText as text

#OLD LINK _______________________________________________________________________

link = "https://www.nytimes.com/column/learning-word-of-the-day" #Get the link for today's word from the general WOTD page
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


for tag in div_container.find_all('h2'): #Line containing the word & part of speech
    ripped = tag.text

headLine = ripped.split("\\")
word = headLine[0].strip()
part = headLine[2].strip()

#IPA Lookup __________________________________________________________________

msg = word + "\n\nPart of Speech:\n" + part #The message that will eventaually be sent as the email body. This will be gradually added to as the program progresses

logfile = open('/home/zach/Desktop/WOTD/ipa.txt', 'r')
loglist = logfile.readlines()
logfile.close()

for line in loglist:
    if str(word) in line:
    	pronunciation = line.split("/")[1].strip()
    	msg = msg + "\n\n" + "Pronunciation:\n" + pronunciation
    	break

msg = msg + "\n\n" + "Definition(s): "

for tag in div_container.find_all('p'):
	if tag.text[0].isdigit() or ":" in tag.text[0:10]:
		msg = msg + "\n" + tag.text

msg = msg + "\n\n" + "_____________________________________ \n\n This email is part of a mailing list. If you would like to be removed from it or wish to subscribe another email address, please send a request to snippythelobster@gmail.com"


#import pdb; pdb.set_trace()


#EMAIL _________________________________________________________________________

print(msg)

