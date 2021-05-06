import socket

SERVER_HOST = 'localhost'
SERVER_PORT = 8006
BUFFER_SIZE = 1024 * 1000

server = socket.socket()
server.connect((SERVER_HOST, SERVER_PORT))

print("Connected!")

while True:
	message = server.recv(BUFFER_SIZE).decode()
	print(message)
	
	yaml = ""
	print("YAML: ")
	while True:
		line = input()
		if line == "":
			break
		yaml += line + "\n"
	
	print("Sending YAML...")
	
	server.send(yaml.encode())
	
	print("Waiting for response...")
	
	message = server.recv(BUFFER_SIZE).decode()
	print("Received: " + message)
