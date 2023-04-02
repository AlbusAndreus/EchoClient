import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 5004))
while True:
    sock.send(input("Enter what you want to echo").encode())
    data = sock.recv(1020).decode()
    print(data)
sock.close()