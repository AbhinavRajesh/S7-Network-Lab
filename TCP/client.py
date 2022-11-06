# import the required dependencies
import socket

_socket = socket.socket()

# PORT at which the server is running at
PORT=3000
HOST="127.0.0.1"

# Connect to the socket server at 127.0.0.1:3000
_socket.connect((HOST, PORT))
print(f"Connected to server at {HOST}:{PORT}")

# Received in bytes
message_bytes = _socket.recv(1024)

# Bytes decoded to string
message_string = message_bytes.decode()

print(f"Message received from the server: {message_string}")

# Closing the socket connection to server
# Not required but is a good practice
_socket.close()
