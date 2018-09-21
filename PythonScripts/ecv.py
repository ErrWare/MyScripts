import json
import pyperclip
import smtplib
import pyzmail
import sys
import emailhelper

print('Args: ' + str(len(sys.argv)))
with open('mainmail.json','r') as mailFile:
	mailInfo = json.load(mailFile)

# TODO: change client to depend on email extension (gmail, yahoo, etc)
smtpdomain, port = emailhelper.getSMTPDetails(mailInfo['address'])
smtpObj = smtplib.SMTP(smtpdomain, port)
smtpObj.ehlo()
smtpObj.starttls()

smtpObj.login(mailInfo['address'], mailInfo['password'])

smtpObj.sendmail(mailInfo['address'],mailInfo['address'],
				 'Subject: copy\n'+pyperclip.paste())
smtpObj.quit()

