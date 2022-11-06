import socket

HOST="127.0.0.1"
PORT=3000


# To simulate 10 connections to the UDP server
for i in range(10):
    _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message_string = f"Connection from {i}"
    # ALWAYS encode your messages to bytes!
    message_bytes = message_string.encode()
    server_address = (HOST, PORT)

    # Notice how there is no connection to server is made
    # before sending the message to server..
    # It's because it is a UDP connection!
    # sendto => UDP
    # connect and send => TCP
    _socket.sendto(message_bytes, server_address)
    print(f"Sent {message_string} to server")
    # TRY-EXCEPT block so that the client doesn't error out when timeout occurs
    try:
        # Receive buffer size is set to 1024
        # Can be 8, can be anything, but keeping it 1024 is a safe bet
        data, server = _socket.recvfrom(1024)
        print(f"Server sent back a message for connection {i}: {data.decode()}")
    except socket.timeout:
        print(f"Request timed out for connection {i}")  