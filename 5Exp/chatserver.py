# AIM: Applications using TCP sockets (Chat Application)
import socket
import threading

clients = []

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            if not msg:
                break

            print("Received:", msg)

            for c in clients:
                if c != client:
                    c.sendall(msg.encode())

        except:
            break

    if client in clients:
        clients.remove(client)
    client.close()

def chat_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', 55555))
    server.listen(5)

    print("Chat server running on port 55555...")

    while True:
        client, address = server.accept()
        print("Connected:", address)
        clients.append(client)

        threading.Thread(
            target=handle_client,
            args=(client,),
            daemon=True
        ).start()

if __name__ == '__main__':
    chat_server()