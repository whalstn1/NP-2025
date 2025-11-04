import socket

class TimeClient:
    def __init__(self, server_ip='172.17.244.150', server_port=5000):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def request_time(self):
        self.client_socket.connect((self.server_ip, self.server_port))
        data = self.client_socket.recv(1024)
        print("[CLIENT] Current server time:", data.decode())
        self.client_socket.close()


if __name__ == "__main__":
    client = TimeClient()
    client.request_time()
