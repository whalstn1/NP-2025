import socket
import datetime

class TimeServer:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"[SERVER] TimeServer started on {self.host}:{self.port}")

        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"[SERVER] Connected by {addr}")
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        # 현재 시간 전송
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client_socket.sendall(current_time.encode())
        print(f"[SERVER] Sent time: {current_time}")
        client_socket.close()


if __name__ == "__main__":
    server = TimeServer()
    server.start()
