import socket, threading

_socket = socket.socket()

# Get the HOSTNAME so that we can get the IP address of the HOST
HOSTNAME=socket.gethostname()
# We need this IP so that other devices connected in the same 
# network can access our server 
HOST_IP=socket.gethostbyname(HOSTNAME)
# PORT of the server
PORT=3000

HOST="127.0.0.1"

_socket.connect((HOST, PORT))
print(f"Connected to server at port: {PORT}")
print(f"Your IP address: {HOST_IP}")

# Input the name of the user connected
name = input("Enter your name: ")

_socket.send(name.encode())
print(f"{name} connected to the server!")

# Function to send messages to the server
def send_message():
    while True:
        message = input(f"\n<{name}>: ")
        # type "exit" to close the client connection to server
        if message == "exit":
            _socket.close()
            print("Closing connection with server...")
        else:
            _socket.send(message.encode())

# Function to listen to messages sent by the user and display
def listen_for_messages():
    while True:
        # Decoding the message to string
        message = _socket.recv(1024).decode()
        print(f"\n<Server> {message}")
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