from socket import *
# For execute python files in python file.
import subprocess
import time

serverPort = 12017
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print(sentence, time.ctime()[11:19])
    connectionSocket.close()
