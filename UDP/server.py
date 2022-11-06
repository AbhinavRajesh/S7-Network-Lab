import socket

PORT=3000

_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Check ../TCP/server.py for explanation
_socket.bind(('', PORT))
print(f"Socket created & binded successfully to port {PORT}")

while True:
    message, address = _socket.recvfrom(1024)
    # Send back to the client at address={address}
    # Sending back the same message sent by client in uppercase
    _socket.sendto(message.decode().upper().encode(), address)


