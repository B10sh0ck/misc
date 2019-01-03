import poplib # recv email
import os # change dir
import time # sleep
import string, random
import StringIO, rfc822
import email.parser
import thread # execute file
import keyboard
import base64
import zipfile

def login():
	USER = "nhanvien05@dientap.cnsc"
	PASSWORD = "41879gY@"
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

def unzipFile(name):
	if name and ('.zip' in name):
		with zipfile.ZipFile(name, 'r') as zip_ref:
			zip_ref.extractall()

def openFile(name):
	if name and ('.docm' in name):
		print 'Opening doc file'
		thread.start_new_thread(os.system, (name, ))
		time.sleep(2)
		keyboard.press_and_release('enter')
		time.sleep(2)
		keyboard.press_and_release('esc')
		time.sleep(2)
		#enable editing
		keyboard.press_and_release('alt+f')
		time.sleep(2)
		keyboard.press_and_release('right')
		time.sleep(2)
		keyboard.press_and_release('down')
		time.sleep(2)
		keyboard.press_and_release('enter')
		time.sleep(2)
		keyboard.press_and_release('enter')
		time.sleep(2)
		keyboard.press_and_release('esc')
		time.sleep(2)
		keyboard.press_and_release('esc')
		time.sleep(2)
		keyboard.press_and_release('alt+f')
		time.sleep(2)
		keyboard.press_and_release('right')
		time.sleep(2)
		keyboard.press_and_release('down')
		time.sleep(2)
		keyboard.press_and_release('enter')
		time.sleep(2)
		keyboard.press_and_release('enter')
		time.sleep(2)
		keyboard.press_and_release('enter')

		print 'Turning off word'
		time.sleep(2)
		os.system('powershell Stop-Process -name WINWORD')
		time.sleep(10)
		os.system('powershell Stop-Process -name cmd')

def readMail(mailbox):
	expected_file = 'votay.zip'
	# list items on server
	resp, items, octets = mailbox.list()

	# get id of the newest email
	id = items[-1].split()[0]

	# get msg of the newest email
	msg = mailbox.retr(id)[1]
	msg = ["\n".join(msg)]
	msg = [email.parser.Parser().parsestr(mssg) for mssg in msg]
	msg = msg[0]

	name = ''
	for part in msg.walk():
		if 'application' in part.get_content_type():
			name = part.get_filename()
			if name == expected_file:
				print 'Downloading %s' % name
				data = part.get_payload(decode=True)
				f = open(name,'wb')
				f.write(data)
				f.close()
				print '%s was downloaded' % name
				unzipFile(name)
				name = name.replace('.zip','.docm')
				openFile(name)	
				print 'Deleting email'
				mailbox.dele(id)
				return True

	time.sleep(5)
	return False

def destroy_evidence():
	try:
		os.remove('votay.docm')
		os.remove('votay.zip')
	except Exception as e:
		print e

def main():
	os.chdir('C:\Users\user\Downloads')
	try:
		os.remove('votay.zip')
		os.remove('votay.docm')
	except Exception as e:
		print ("Exception: " + str(e))

	while True:
		try:
			mailbox = login()
			if mailbox:
				print 'Login successful'
				print "[+] Getting the expected email"
				if readMail(mailbox):
					mailbox.quit()
					print 'Logged out'
					break
				else:
					print "[+] The expected email hasn't arrived"
					mailbox.quit()
					print 'Logged out'
		except Exception as e:
			print ("Login failed: " + str(e))
			time.sleep(3)
			
	# xoa dau vet
	#time.sleep(900)
	print 'Destroying evidence'
	destroy_evidence()
	print 'Done'

main()