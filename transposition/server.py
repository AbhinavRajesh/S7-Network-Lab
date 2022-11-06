import socket, math

PORT=3000

# TODO: DOCUMENT!!
key="ABCD"

def decrypt_message(cipher_text):
    message = ""

    key_index = 0

    message_index = 0
    cipher_length = len(cipher_text)
    # Message characters as a single list
    cipher_list = list(cipher_text)
    print(f"{cipher_list=}")
    # Key characters as a single list
    key_list = sorted(list(key))

    # Number of columns 
    columns = len(key)
    # Max rows of the matrix
    rows = int(math.ceil(cipher_length/columns))

    # Deciphered matrix
    dec_cipher = []
    for _ in range(rows):
        dec_cipher += [[None] * columns]

    print(f"{dec_cipher=}")

    for _ in range(columns):
        current_index = key.index(key_list[key_index])


        for j in range(rows):
            dec_cipher[j][current_index] = cipher_list[message_index]
            print(f"{dec_cipher=}")
            message_index += 1
        key_index += 1
    
    # convert decrypted msg matrix into a string
    try:
        message = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")
  
    null_count = message.count('_')
  
    if null_count > 0:
        return message[: -null_count]
  
    return message

def main():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.bind(("", PORT))

    _socket.listen(10)

    while True:
        client, address = _socket.accept()
        print(f"Received connection from the {address=}")
        message = client.recv(1024).decode()
        print(f"Received encrypted {message=}")

        decrypted_message = decrypt_message(message)
        print(f"Decrypted text: {decrypted_message}")

if __name__ == "__main__":
    main()