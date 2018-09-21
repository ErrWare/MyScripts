import json
import pyperclip
import imapclient
import pyzmail
import emailhelper

with open('mainmail.json','r') as mailFile:
	mailInfo = json.load(mailFile)

imapdomain = emailhelper.getIMAPDetails(mailInfo['address'])
imapObj = imapclient.IMAPClient(imapdomain, ssl=True)

imapObj.login(mailInfo['address'], mailInfo['password'])

imapObj.select_folder('INBOX', readonly=False)

# Get all copy-intended messages
UIDS = imapObj.search(['SUBJECT', 'copy', 'UNSEEN'])

if len(UIDS) == 0:
	print('no messages to copy from')
	exit()

# Fetch only the latest copy message
ID = UIDS[-1]
rawMessages = imapObj.fetch(UIDS[-1:], ['BODY[]'])
# Make message readable
message = pyzmail.PyzMessage.factory(rawMessages[ID][b'BODY[]'])
# Copy to clipboard string version of message
charset = message.text_part.charset
payload = message.text_part.get_payload()
if charset is None:
	text = payload.decode()
else:
	text = payload.decode(charset)

# Avast likes to append stuff to my programmatically made outgoing emails.
text = text.split('\r\n')
text = [line for line in text if not line.startswith('X-Antivirus')]
text = '\r\n'.join(text).strip()
print('Copied: ' + text)
pyperclip.copy(text)

