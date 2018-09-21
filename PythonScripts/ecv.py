import json
import pyperclip
import smtplib
import pyzmail
import sys
import emailhelper

print('Args: ' + str(len(sys.argv)))
with open('mainmail.json','r') as mailFile:
	mailInfo = json.load(mailFile)

smtpdomain, port = emailhelper.getSMTPDetails(mailInfo['address'])
smtpObj = smtplib.SMTP(smtpdomain, port)
smtpObj.ehlo()
smtpObj.starttls()

smtpObj.login(mailInfo['address'], mailInfo['password'])
# determine what to paste
if len(sys.argv) > 1:
	text = ' '.join(sys.argv[1:])
else
	text = pyperclip.paste()
print('Pasted: ' + text)
smtpObj.sendmail(mailInfo['address'],mailInfo['address'],
				 'Subject: copy\n'+text)

smtpObj.quit()



