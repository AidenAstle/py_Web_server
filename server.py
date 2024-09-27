import time
import socket


# SERVER HOST AND IP
# run 'netstat -aon' and find listening TCP port
# run 'ipconfig' to check IPv4 addr
SERVER_HOST = "192.168.1.193"
SERVER_PORT = 8080

# Create a server socket
# AF_INET - for IPv4 protocols
# SOCK_STREAM - TCP 
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ----- LISTENING PORT -----
serverSocket.bind((SERVER_HOST, SERVER_PORT))

# Set the socket to listen to 1 connection at a time, can be altered
serverSocket.listen(1)

# ----- START SERVER -----
while True:
    print("------------------------ SERVER IDLE :: READY TO SERVE ------------------------")
    print(f"Listening on port {SERVER_PORT}")
    time.sleep(10)
    
    client_socket, client_addr = serverSocket.accept()
    print(f"Cli Socket : {client_socket} \nCli IP : {client_addr}")
    request = client_socket.recv(1500).decode()
    print(request)