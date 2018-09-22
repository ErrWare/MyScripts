import json
import pyperclip
import smtplib
import pyzmail
import sys
import emailhelper
import os
import inspect

print('Args: ' + str(len(sys.argv)))
py_dir = os.path.dirname(inspect.stack()[0][1])
with open(os.path.join(py_dir,'mainmail.json'),'r') as mailFile:
	mailInfo = json.load(mailFile)

smtpObj, _ = emailhelper.login(mailInfo)

# determine what to paste
if len(sys.argv) > 1:
	text = ' '.join(sys.argv[1:])
else:
	text = pyperclip.paste()
print('Pasted: ' + text)
smtpObj.sendmail(mailInfo['address'],mailInfo['address'],
				 'Subject: copy\n'+text)

smtpObj.quit()



