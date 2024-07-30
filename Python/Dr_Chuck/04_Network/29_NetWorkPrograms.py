import socket

# Create a new socket object using IPv4 and TCP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the remote server
# 'data.pr4e.org' is the hostname of the server
# Port 80 is the default port for HTTP traffic
mysock.connect(('data.pr4e.org', 80))

# Formulate the HTTP GET request
# '\r\n' is used to properly terminate the lines in the HTTP request
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

# Send the HTTP GET request to the server
mysock.send(cmd)

# Receive and print the response from the server
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

# Close the socket connection
mysock.close()





