from string import ascii_lowercase
import socket			

# Create a socket object
_socket = socket.socket()		

# Define the PORT on which you want to connect
PORT = 3000			
HOST = "127.0.0.1"
# Connect to the server on local computer
_socket.connect((HOST, PORT))

# Function to encode the message
def encode(plain_text, key):
    alphabets = ascii_lowercase
    cipher_text = ""
    for i in plain_text:
        if i == " ":
            cipher_text += i
        else:
            # Find the encoding of the character and append it to cipher text
            cipher_text += alphabets[(alphabets.index(i) + key) % 26]
    return cipher_text

def main():
    plain_text = input("Enter the plain text: ")
    key = int(input("Enter key(integer): "))

    print(f"Entered {plain_text=}")
    print(f"Entered {key=}")

    cipher_text = encode(plain_text, key)
    print(f"Cipher text sent: {cipher_text}")

    _socket.send(f"{cipher_text};{key}".encode())
    _socket.close()

main()

