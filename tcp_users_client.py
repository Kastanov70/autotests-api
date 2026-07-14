import socket


messages = ["Привет, сервер!", "Как дела?"]


for message in messages:
    # Создаем TCP-сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Подключаемся к серверу
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)
    # Отправляем сообщение серверу
    client_socket.send(message.encode())

    # Получаем ответ от сервера
    response = client_socket.recv(1024).decode()
    print(f"{response}")

    # Закрываем соединение
    client_socket.close()
