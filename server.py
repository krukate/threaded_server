import socket
import threading


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.send(data)


def echo_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"Прослушивает порт {host}:{port}")

    while True:
        client, addr = server.accept()
        print(f"Добавлено соединение {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 9090
    echo_server(HOST, PORT)