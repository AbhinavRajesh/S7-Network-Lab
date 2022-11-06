from string import ascii_lowercase
import socket			

# Create a socket object
_socket = socket.socket()		

# Define the PORT on which you want to connect
PORT = 3000			
# Connect to the server on local computer
_socket.bind(("", PORT))
_socket.listen(1)

# Function to encode the message
def decode(cipher_text, key):
    alphabets = ascii_lowercase
    plain_text = ""
    for i in cipher_text:
        if i == " ":
            plain_text += i
        else:
            # Find the decoding of the character and append it to plain text
            plain_text += alphabets[(alphabets.index(i) - key) % 26]
    return plain_text

def main():
    while True:
        client, address = _socket.accept()
        print(f"Got connection from {address=}")

        data = client.recv(1024).decode()

        if not data:
            break

        cipher_text, key = data.split(";")
        plain_text = decode(cipher_text.lower(), int(key))
        print(f"Received {cipher_text=}")
        print(f"Received {key=}")
        print(f"Decoded text: {plain_text}")
        client.close()

main()

