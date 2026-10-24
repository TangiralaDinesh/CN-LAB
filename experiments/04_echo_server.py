"""Local TCP echo server for experiment 4."""

import socket

HOST = "127.0.0.1"
PORT = 65432


def serve() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"Echo server listening on {HOST}:{PORT}")
        connection, address = server.accept()
        with connection:
            print(f"Connected by {address}")
            reader = connection.makefile("rb")
            while line := reader.readline():
                connection.sendall(line)
                if line.strip().lower() in (b"bye", b"exit"):
                    break


if __name__ == "__main__":
    serve()
