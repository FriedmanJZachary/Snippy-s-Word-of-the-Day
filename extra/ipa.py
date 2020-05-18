#!/usr/bin/env python3

#IPA lookup courtosey of: https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/en_US.txt

logfile = open('ipa.txt', 'r')
loglist = logfile.readlines()
logfile.close()

for line in loglist:
    if str('potato') in line:
    	pronunciation = line.split("/")[1].strip()
    	print(pronunciation)
    	break
