# Fuzzing.py
A python script for testing the BufferOver-flow vulnerability on a system. 



At line 10-you have to provide the payload name or the commands that are running on the server.
At line 13- you have to provide the Ip address and port.


#BufferOverflow

##Stack is Divided into four parts-

###ESP(Extended Stack Pointer)

###BufferSpace

###EBP(Extended Base Pointer)

###EIP(Extended Instruction Pointer)

So,what this script does it sends out characters to the **bufferspace**  and keep sending until it is filled and if a system will have **buffer-overflow Vulnerability** it will also send the characters to **EBP** and **EIP** and then the system will crash.

##If this Vulnerability is present then the attacker can  overwrite the **EIP** and create a reverse shell and gain access to the system.
