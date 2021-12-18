#Visal Hak(13479151),Gongming Shi (13713654), Joyee Lin (13882535)
#Network Fundamental project 1, Simple web server

#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 1025
serverSocket.bind(('10.0.0.25', serverPort))
serverSocket.listen(1)
statusOK = "HTTP/1.1 200 OK\r\n" \
           "Content-Type: text/html\r\n\r\n"
status404 = "HTTP/1.1 404 Not Found\r\n\r\n"
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        #Send one HTTP header line into socket
        connectionSocket.send(statusOK.encode())
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send(status404.encode())
        #Close client socket
        connectionSocket.close()
serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data
