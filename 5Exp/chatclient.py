# AIM: TCP Chat Client
import socket
import threading

def receive_messages(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            if not msg:
                break
            print("\nReceived:", msg)
        except OSError:
            break

def chat_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 55555))

    print("Connected to chat server!")
    threading.Thread(
        target=receive_messages,
        args=(client,),
        daemon=True
    ).start()

    try:
        while True:
            msg = input("Enter message (exit to quit): ")

            if msg.lower() == "exit":
                break

            client.sendall(msg.encode())
    except (OSError, EOFError, KeyboardInterrupt):
        pass
    finally:
        client.close()
        print("Disconnected from server.")

if __name__ == '__main__':
    chat_client()