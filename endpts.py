import socket, time, logging

# CONFIG
logging.basicConfig(filename='server.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S:%MS')
logger = logging.getLogger()

# function to handle GET requests from client in server.py
def http_GET(file_path):
    if(file_path[0] != '/'):
        return throw404()
    file_path = 'static' + file_path + '.html'
    try:
        fin = open(file_path)
    except FileNotFoundError:
        fin = open('static/404.html')
    content = fin.read()
    fin.close()
    response = 'HTTP/1.1 200 OK\n\n' + content
    logger.debug(response)
    return response.encode()

    
def http_POST(file_path):
    return response.encode()


def http_PUT(file_path):
    return response.encode()

    
def throw404():
    fin = open('static/404.html')
    content = fin.read(); fin.close()
    response = 'HTTP/1.1 404 Not Found\n\n' + content
    logger.debug("404 Not Found")
    return response.encode()