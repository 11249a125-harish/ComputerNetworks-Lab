# AIM : To Write a program to identify the machine's hostname and IP Address
import socket
hostname = socket.gethostname()
ip_address=socket.gethostbyname(hostname)
print("Hostname:",hostname)
print("IP Address:",ip_address)
