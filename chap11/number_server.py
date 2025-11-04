import socket

class NumberServer:
    def __init__(self, host='0.0.0.0', port=7000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"[SERVER] NumberServer started on {self.host}:{self.port}")

        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"[SERVER] Connected by {addr}")
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            msg = data.decode().strip()
            print(f"[SERVER] Received: {msg}")

            if msg.lower() == 'exit':
                print("[SERVER] Client requested to close connection.")
                break

            # 숫자 계산 (제곱)
            try:
                number = float(msg)
                result = number ** 2
                response = f"The square of {number} is {result}"
            except ValueError:
                response = "Please send a valid number."

            client_socket.sendall(response.encode())
        client_socket.close()


if __name__ == "__main__":
    server = NumberServer()
    server.start()
