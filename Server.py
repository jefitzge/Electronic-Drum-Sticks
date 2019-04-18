# SOURCE: https://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/
# Modified ClientThread to play local sound file based on data recieved

import pygame as pygame
from pygame import mixer
import socket
from threading import Thread
from socketserver import ThreadingMixIn
from playsound import playsound

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print ("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):
        while True:
            data = conn.recv(2048)
            data = str(data, encoding="utf-8")
            # print("Server received data:", data)
            if data == '1':
                print('A')
                playsound('/Users/jofit/Desktop/ElectricDrums/drumdemo/Sounds/Tom_modified.wav')
            if data == '2':
                print('B')
                playsound('/Users/jofit/Desktop/ElectricDrums/drumdemo/Sounds/Cymbol_modified.wav')
            if data == '3':
                print('C')
                playsound('/Users/jofit/Desktop/ElectricDrums/drumdemo/Sounds/Hat_modified.wav')
            if data == '4':
                print('D')
                playsound('/Users/jofit/Desktop/ElectricDrums/drumdemo/Sounds/Snare_modified.wav')



# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0'
TCP_PORT = 2004
BUFFER_SIZE = 20  # Usually 1024, but we need quick response

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Hostname :  ", host_name)
print("IP : ", host_ip)

while True:
    print()
    tcpServer.listen(4)
    print( "Multithreaded Python server : Waiting for connections from TCP clients...")
    (conn, (ip, port)) = tcpServer.accept()

    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()

