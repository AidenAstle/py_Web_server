from socket import *

# Create a server socket
# AF_INET - for IPv4 protocols
# SOCK_STREAM - TCP 
serverSocket = socket(AF_INET, SOCK_STREAM)

# ----- LISTENING PORT -----
# run 'netstat -aon' and find listening TCP port
serverPort = 1492

# 