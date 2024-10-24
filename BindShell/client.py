#Made by sug023
#!/bin/env python
import socket; from colorama import Fore as color

# Put the target ip and the port
PORT = 6666
IP = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((IP, PORT))

print(color.GREEN+f"[+]{color.WHITE} Connection established with{color.YELLOW} {IP}{color.WHITE} on port{color.YELLOW} {PORT}{color.WHITE} :)"+color.RESET)

while True:
    cmd = input(color.CYAN+f"\n$:{color.WHITE} "); cmd = cmd.encode("utf-8")
    client.send(cmd)
    output = client.recv(1024); output = output.decode("utf-8"); print(color.YELLOW+f"\n{output}")
    
