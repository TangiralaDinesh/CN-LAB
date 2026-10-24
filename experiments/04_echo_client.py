"""TCP echo client for experiment 4."""

import socket

HOST = "127.0.0.1"
PORT = 65432


def main() -> None:
    with socket.create_connection((HOST, PORT)) as connection:
        reader = connection.makefile("rb")
        while True:
            message = input("Message (bye/exit to stop): ")
            connection.sendall((message + "\n").encode("utf-8"))
            echoed = reader.readline()
            if not echoed:
                print("Server closed the connection.")
                break
            print(f"Echoed: {echoed.decode('utf-8').rstrip()}")
            if message.strip().lower() in ("bye", "exit"):
                break


if __name__ == "__main__":
    main()
