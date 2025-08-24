import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345

server_socket.bind((host, port))

server_socket.listen(5)
print(f"Servidor esperando a conexao no host {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Conexão aceita de {addr}")
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Mensagem recebida: {message}")
    client_socket.send("Mensagem recebida".encode('utf-8'))
    client_socket.close()