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
		mailbox = poplib.POP3_SSL(SERVER)
		 
		# login
		mailbox.user(USER)
		mailbox.pass_(PASSWORD)
	except Exception as ex:
		print (ex)
		return None

	return mailbox

def readMail(server):
	expected_file = 'votay.docm'

	# list items on server
	resp, items, octets = server.list()
	print (resp, items, octets)
	exit()
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
			if name == expected_file:
				print 'Downloading %s' % name
				data = part.get_payload(decode=True)
				f = open(name,' wb')
				f.write(data)
				f.close()
				print 'Downloaded %s' % name
				break

	if name and ('.docm' in name):
		print 'Opening doc file'
		thread.start_new_thread(os.system, (name, ))
		time.sleep(2)
		keyboard.press_and_release('esc')
		time.sleep(1)
		#enable editing
		keyboard.press_and_release('alt+f')
		time.sleep(1)
		keyboard.press_and_release('right')
		time.sleep(1)
		keyboard.press_and_release('down')
		time.sleep(1)
		keyboard.press_and_release('enter')
		time.sleep(1)
		keyboard.press_and_release('esc')
		time.sleep(1)
		keyboard.press_and_release('esc')

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
	return Fals

def main():
	os.chdir('C:\Users\Administrator\Downloads')
	try:
		os.remove('votay.docm')
	except Exception as e:
		print e

	# print "[+] Waiting start command ... "
	# #wait(5)
	# print "[+] Received start command"

	while True:
		try:
			mailbox = login()
			if mailbox:
				print 'Login success'
				print "[+] Receiving expected email"
				if readMail(mailbox):
					mailbox.quit()
					print 'Logged out'
					break
				else:
					print "[+] The expected email didn't arrive"

				mailbox.quit()
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
		mailbox = login()
		if mailbox:
			print ("Succeed")
		else:
			print ("Failed")
	except Exception as e:
		print (e)

main()