# Aiden's Web Server

This is my web server, not a whole lot else to say right now. Instructions will follow.


## Lauch

In the 'server.py' file exist variables SERVER_HOST & SERVER_PORT, the port can remain 8080, 
but ensure the host reflects the host machine's current IPv4 address. To find this you can run 
'ipconfig' from your cmd prompt. Set these values and you are good to run the server from the 
'server.py' file.

### INFO
Currently only supports standard HTTP/1.1 GET requests. The 'index.html' or '/' directory 
contains a list of all available pages hosted. To reach any of them, just append their name 
to the end of your search, ex. 100.1.1.13:8080/home to view 'home.html'.

### Roadmap
- Accept POST and PUT requests  
- Add more files and support more filetypes  
- More pleasant looking pages(REACT or similar)  
- Refactor server.py