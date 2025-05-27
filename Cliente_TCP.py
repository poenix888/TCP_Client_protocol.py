import socket

target_host = "www.google.com"
target_port = 80

# criar un objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conectar ao cliente
client.connect((target_host,target_port))

# enviar alguns dados
client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

# receber alguns dados
response = client.recv(4096)

print(response.decode())
