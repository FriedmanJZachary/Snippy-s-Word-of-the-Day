#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import smtplib, ssl
from email.mime.text import MIMEText as text


link = "https://www.etymonline.com/word/lick"
data = requests.get(link).text
soup = BeautifulSoup(data, features="html.parser")
div_container = soup.find_all("div", {"class": "word--C9UPa"})

msg = ""

for container in div_container:  #For each block containing a word form and etymology
    for tag in container.find_all(attrs={"class": "word__name--TTbAA"}): #For all word form titles
        msg = msg + "\n" + tag.text + "\n"

    for body in container.find_all(attrs={"word__defination--2q7ZH"}): #Find all body sections (that contain the actual etymologies)
        for paragraph in body.find_all("p"):
            msg = msg + paragraph.text

    msg = msg + "\n"

print(msg)

