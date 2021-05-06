import socket
import yaml
import subprocess

SERVER_HOST = 'localhost'
SERVER_PORT = 8006
BUFFER_SIZE = 1024 * 1000

server_socket = socket.socket()
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

print("Waiting for connection...")

client_socket, client_address = server_socket.accept()

print("Found a connection!")

while True:
	message = "Send YAML to decode!\n"
	client_socket.send(message.encode())
	
	print("Waiting for YAML...")
	
	input = client_socket.recv(BUFFER_SIZE).decode()
	
	print("Got YAML! Decoding now...")
	
	output = yaml.load(input, Loader=yaml.Loader)
	
	print("Sending YAML.")
	
	client_socket.send((str(output) + "\n").encode())
