import socket


def echo_client(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        message = input("Введите сообщение для отправки (или 'exit' чтобы выйти): ")
        if message.lower() == 'exit':
            break
        client.send(message.encode())

        response = client.recv(1024)
        print(f"Получено: {response.decode()}")

    client.close()


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 9090
    echo_client(HOST, PORT)