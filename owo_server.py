# -*- coding: utf-8 -*-
import socket
import os
import re
import datetime

regex = re.compile("(([uUoOvV][wW][uUoOvV])*([uUoO][vV][uUoO])*(:3)*( )*)+")
sock = "/tmp/owosock"
if os.path.exists(sock):
    os.remove(sock)

print("Opening socket...")
server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server.bind(sock)
os.chmod(sock,1410)

print("Listening...")
while True:
    datagram = server.recv(1024)
    if not datagram:
        break
    else:
        user = datagram.decode('utf-8')
        owo = f'/pub/{user}/owomessage.txt'

        if not os.path.isfile(owo):
            print("sowwy no worky: error no uwu")
            continue;

        owo = open(owo, "r")
        txt = owo.read().strip()

        if re.fullmatch(regex, txt):
            print(f":3 owo {user}");
            with open("/pub/hammy/http/owo/index.html", "a") as myfile:
                time = str(datetime.datetime.now())
                myfile.write(f'{txt} - {user} @ {time} \n')

print("-" * 20)
print("Shutting down...")
server.close()
os.remove("/tmp/owosock")
print("Done")
