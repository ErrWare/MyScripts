import re
import imapclient
import smtplib

if __name__ == '__main__':
	print('This module helps get get the right imap and smtp connections for various emails')

def getDomain(email):
	domainRE = re.compile('@([a-z]+).')
	mo = domainRE.search(email)
	if mo is None:
		print('no domain found')
		return None
	return mo.group(1)

# I don't know what the @domain actually is
def getSMTPDetails(email):
	domain = getDomain(email)
	if domain == 'gmail':
		return 'smtp.gmail.com', 587
	if domain == 'yahoo':
		return 'smtp.mail.yahoo.com', 587
	if domain == 'hotmail':	#outlook??
		return 'smtp-mail.outlook.com', 587
	if domain == 'att':	#AT&T??
		return 'smtp.mail.att.net', 465
	if domain == 'comcast':	#??
		return 'smtp.comcast.net', 587
	if domain == 'verizon':	#??
		return 'smtp.verizon.net', 465
	
	print('Domain Name ' + str(domain) + ' not recognized')
	return None, None

def getIMAPDetails(email):
	domain = getDomain(email)
	if domain == 'gmail':
		return 'imap.gmail.com'
	if domain == 'yahoo':
		return 'imap.mail.yahoo.com'
	if domain == 'hotmail':	#outlook??
		return 'imap-mail.outlook.com'
	if domain == 'att':	#AT&T??
		return 'imap.mail.att.net'
	if domain == 'comcast':	#??
		return 'imap.comcast.net'
	if domain == 'verizon':	#??
		return 'imap.verizon.net'

	print('Domain Name ' + str(domain) + ' not recognized')
	return None

def loginSMTP(mailInfo):
	smtpdomain, port = getSMTPDetails(mailInfo['address'])
	smtpObj = smtplib.SMTP(smtpdomain, port)
	smtpObj.ehlo()
	smtpObj.starttls()

	smtpObj.login(mailInfo['address'], mailInfo['password'])
	return smtpObj

def loginIMAP(mailInfo):
	imapdomain = getIMAPDetails(mailInfo['address'])
	imapObj = imapclient.IMAPClient(imapdomain, ssl=True)

	imapObj.login(mailInfo['address'], mailInfo['password'])
	return imapObj


def login(mailInfo):
	smtpObj = loginSMTP(mailInfo)
	imapObj = loginIMAP(mailInfo)
	return smtpObj, imapObj

