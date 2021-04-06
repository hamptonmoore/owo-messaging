#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import os
import re
import getpass

rawregex = "(([uUoOvV][wW][uUoOvV])*([uUoO][vV][uUoO])*(:3)*( )*)+"
regex = re.compile(rawregex)

user = getpass.getuser()

print("Connecting...")
if os.path.exists("/tmp/owosock"):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect("/tmp/owosock")

    message = input(f'Hewwo {user}, pwease tywpe youw mesage for the boawd: ')

    if not re.fullmatch(regex, message):
        print(f'please type an owo message with the following regex {rawregex}')
    
    owomessage = f'/pub/{user}/owomessage.txt'
    f = open(owomessage, "w")
    f.write(message)
    f.close()

    client.send(user.encode('utf-8'))
else:
    print("owo server is down :( yell at hammy on IRC")

