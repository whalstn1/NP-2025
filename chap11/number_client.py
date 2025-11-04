import socket

class NumberClient:
    def __init__(self, server_ip='127.0.0.1', server_port=7000):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.client_socket.connect((self.server_ip, self.server_port))
        print("[CLIENT] Connected to NumberServer.")
        print("Type 'exit' to quit.\n")

        while True:
            msg = input("Enter a number: ")
            self.client_socket.sendall(msg.encode())
            if msg.lower() == "exit":
                break
            data = self.client_socket.recv(1024)
            print("[CLIENT] Server response:", data.decode())

        self.client_socket.close()


if __name__ == "__main__":
    client = NumberClient()
    client.start()
