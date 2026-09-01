# Servidor
import socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0", 5000))
servidor.listen()
while True:
    cliente, endereco = servidor.accept()
    dados = cliente.recv(1024)
    print(f"Cliente {endereco} enviou {dados.decode('utf-8')}")
    cliente.close()
servidor.close()