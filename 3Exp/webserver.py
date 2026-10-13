# AIM: To write a HTTP web client Program to download a webpage using TCP Sockets

import socket
# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the server to localhost and port 8080
server.bind(('localhost', 8080))
# Listen for incoming connections
server.listen(1)
print("HTTP Server running on http://localhost:8080 ...")
while True:
    # Accept a client connection
    conn, addr = server.accept()
    print(f"Connected by {addr}")
    # Receive the HTTP request
    request = conn.recv(1024).decode()
    print("--- Received HTTP Request ---")
    print(request)
    # Build a valid HTTP response
    http_response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        "Connection: close\r\n"
        "\r\n"
        "<html><body>"
        "<h1>Welcome to Computer Networks Lab!</h1>"
        "</body></html>"
    )
    # Send the HTTP response
    conn.sendall(http_response.encode())
    # Close the client connection
    conn.close()