import socket

class EchoClient:
    def __init__(self, server_ip='127.0.0.1', server_port=6000):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.client_socket.connect((self.server_ip, self.server_port))
        print("[CLIENT] Connected to EchoServer.")
        print("Type 'exit' to quit.\n")

        while True:
            msg = input("Enter message: ")
            if msg.lower() == "exit":
                break
            self.client_socket.sendall(msg.encode())
            data = self.client_socket.recv(1024)
            print("[CLIENT] Echo from server:", data.decode())

        self.client_socket.close()


if __name__ == "__main__":
    client = EchoClient()
    client.start()
