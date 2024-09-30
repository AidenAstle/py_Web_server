import socket, time, logging, json, http.server
import endpts


# ------CONFIG------
logging.basicConfig(filename='server.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger()

# SERVER HOST AND IP
# run 'netstat -aon' and find listening TCP port
# run 'ipconfig' to check IPv4 addr
# 192.168.1.193:8080
host_name = socket.gethostname()
host_ip = (socket.gethostbyname_ex(host_name)[2])[0]
logger.info(f"HOST_NAME : {host_name}\tHOST_IP: {host_ip}")
SERVER_HOST = host_ip
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
    logger.debug("------------------------ SERVER IDLE :: READY TO SERVE ------------------------")
    logger.debug("Listening on port : 8080")
    
    client_socket, client_addr = serverSocket.accept()
    request = client_socket.recv(1500).decode()
    logger.debug(request)
    
    # PULL first header, prolly GET
    headers = request.split('\n') 
    http_method = (headers[0].split())[0]
    path = (headers[0].split())[1]
    # print(f"HTTP METHOD : {http_method} \nPATH : {path}")
    
    # ------ STANDARD HTTP RESPONSE ------
    # STATUS LINE -
    # HEADERS
    # MESSAGE-BODY
    
    if http_method == 'GET':
        if path == '/':
            response = endpts.http_GET('/index')
            client_socket.sendall(response)
            client_socket.close()
        else:
            response = endpts.http_GET(path)
            client_socket.sendall(response)
            client_socket.close() 
    else:
        response = 'HTTP/1.1 405 Method Not Allowed\n\nALLOW: GET'
        logger.debug(response)
        client_socket.sendall(response.encode())
        client_socket.close()
    logger.debug('-------- Client Socket Connection Closed --------')