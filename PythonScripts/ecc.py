import json
import pyperclip
import imapclient
import pyzmail


with open('mainmail.json','r') as mailFile:
	mailInfo = json.load(mailFile)

# TODO: change client to depend on email extension (gmail, yahoo, etc)
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

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
pyperclip.copy(message.text_part.get_payload().decode(message.text_part.charset))
