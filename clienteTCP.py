# Cliente
import socket
import time

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1", 5000))
cliente.send("/cpu".encode())
dados, conn = cliente.recvfrom(1024)
print(dados.decode())
cliente.close()