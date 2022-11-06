import socket, threading
import sys

_socket = socket.socket()

# Get the HOSTNAME so that we can get the IP address of the HOST
HOSTNAME=socket.gethostname()
# We need this IP so that other devices connected in the same 
# network can access our server 
HOST_IP=socket.gethostbyname(HOSTNAME)
# PORT of the server
PORT=3000

# Check ../TCP/server.py line 08-11
_socket.bind(('', PORT))

print(f"Successfully binded the server at port: {PORT}")
print(f"Your IP address: {HOST_IP}")

# Input the name of the user connected
name = input("Enter your name: ")
_socket.listen(1)

# For accepting the single connection in single client chat program
client, address = _socket.accept()
print(f"{address} connected to the server!")

# Get name of the client
client_name = client.recv(1024).decode()
print(f"{client_name} connected to the server!")


# Function to send messages to the server
def send_message():
    while True:
        message = input(f"\n<{name}> ")
        # type "exit" to close the client connection to server
        if message == "exit":
            client.close()
            print("Closing connection with server...")
        else:
            client.send(message.encode())

# Function to listen to messages sent by the user and display
def listen_for_messages():
    while True:
        # Decoding the message to string
        message = client.recv(1024).decode()
        print(f"\n<{client_name}> {message}")
        if message == "exit":
            _socket.close()
            print("Closing connection with server...")


# Why threading you may ask?
# Threading is the proccess through which you can run 
# multiple lines of code simultaneously
# 
# Here we need 2 threads
# 1. For listening to the message sent by the server
# 2. For listening to the input from user

# This thread listens to the message sent by the server
listen_message_thread = threading.Thread(target=listen_for_messages)
listen_message_thread.start()

# This thread listens to the message sent by the user
send_message_thread = threading.Thread(target=send_message)
send_message_thread.start()