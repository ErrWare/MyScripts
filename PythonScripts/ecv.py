import json
import pyperclip
import smtplib
import pyzmail


with open('mainmail.json','r') as mailFile:
	mailInfo = json.load(mailFile)

# TODO: change client to depend on email extension (gmail, yahoo, etc)
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

smtpObj.login(mailInfo['address'], mailInfo['password'])

smtpObj.sendmail(mailInfo['address'],mailInfo['address'],
				 'Subject: copy\n'+pyperclip.paste())
smtpObj.quit()

