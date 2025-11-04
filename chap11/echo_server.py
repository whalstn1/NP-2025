import socket

class EchoServer:
    def __init__(self, host='0.0.0.0', port=6000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"[SERVER] EchoServer started on {self.host}:{self.port}")

        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"[SERVER] Connected by {addr}")
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"[SERVER] Received: {data.decode()}")
            client_socket.sendall(data)  # 그대로 반송 (Echo)
        client_socket.close()


if __name__ == "__main__":
    server = EchoServer()
    server.start()
