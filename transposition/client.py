import socket, math

HOST="127.0.0.1"
PORT=3000

# TODO: DOCUMENT!!
key="ABCD"

def encrypt_message(message) -> str:
    cipher_text = ""

    key_index = 0

    message_length = len(message)
    # Message characters as a single list
    message_list = list(message)
    # Key characters as a single list
    key_list = sorted(list(key))

    # Number of columns 
    columns = len(key)
    # Max rows of the matrix
    rows = int(math.ceil(message_length/columns))

    # Fill empty cells with "_"
    fill_null = int((rows*columns)-message_length)
    message_list.extend("_"*fill_null)
    # Matrix for columnar transposition cipher is created
    matrix = [message_list[i:i+columns] for i in range(0, len(message_list), columns)]
    
    # Read column-wise using the key
    for _ in range(columns):
        current_index = key.index(key_list[key_index])
        cipher_text += "".join([row[current_index] for row in matrix])
        key_index += 1
    
    return cipher_text

def main():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.connect((HOST, PORT))

    while True:
        message = input("Enter the plain text: ")
        encrypted_message = encrypt_message(message)
        print(f"Generated encrypted text: {encrypted_message}")
        _socket.send(encrypted_message.encode())
        print("Encrypted message sent!")

if __name__ == "__main__":
    main()