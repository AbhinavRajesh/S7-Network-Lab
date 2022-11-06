import socket

_socket = socket.socket()

# PORT at which the server SHOULD run
PORT=3000

# Leaving the host as empty so that it is available to everyone
# connected to the network. Others can access using the IP address
# the machine in the HOST of client
# Eg. in client, HOST="192.168.x.x"
_socket.bind(('', PORT))
print(f"Socket created & binded successfully to port {PORT}")

_socket.listen(5)
print("Socket is listening for connections...")

# For running the server forever
while True:
    # Loop will wait here forever till a connection is established
    # client refers to the connected client (Duh..)
    # address is the address from where the connection is made
    client, address = _socket.accept()

    print(f"Received connection from the address {address}")
    message_to_send = "Thank you for connecting with the server! Have a great day!"

    # NOTE: ALWAYS encode the message you are sending...
    # Message should be in the form of BYTES and not string!
    client.send(message_to_send.encode())
    
    # Close the connection made with the client after sending the message
    # You might want to keep it open if it was a chat application
    client.close()

    # Close the server after 1 client is connected..
    # Remove the following "break" if you want the server to not
    # kill itself after only 1 connection
    break