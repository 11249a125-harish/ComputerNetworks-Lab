# AIM: To transfer a file from a client to a server using TCP sockets.

import socket
import os

def file_transfer_client():
    filename = input("Enter the filename to send: ")

    if not os.path.isfile(filename):
        print("File not found!")
        return

    client_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )

    client_socket.connect(('localhost', 12345))
    client_socket.sendall(filename.encode())

    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(1024)

            if not chunk:
                break

            client_socket.sendall(chunk)

    print("File sent successfully.")
    client_socket.close()

if __name__ == '__main__':
    file_transfer_client()


