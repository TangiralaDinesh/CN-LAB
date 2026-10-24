"""Threaded local TCP chat server/client for experiment 5."""

import argparse
import socket
import threading

HOST = "127.0.0.1"
PORT = 65433
MAX_LINE = 4096
clients: dict[socket.socket, tuple[str, object]] = {}
clients_lock = threading.Lock()


def broadcast(message: str, skip: socket.socket | None = None) -> None:
    payload = (message + "\n").encode("utf-8")
    stale = []
    with clients_lock:
        for connection, (_, writer) in clients.items():
            if connection is skip:
                continue
            try:
                writer.write(payload)
                writer.flush()
            except OSError:
                stale.append(connection)
        for connection in stale:
            clients.pop(connection, None)
            connection.close()


def handle_client(connection: socket.socket, address: tuple[str, int]) -> None:
    with connection:
        reader = connection.makefile("rb")
        name_line = reader.readline(MAX_LINE + 1)
        name = name_line.decode("utf-8", errors="replace").strip()[:40] or str(address[0])
        writer = connection.makefile("wb")
        with clients_lock:
            clients[connection] = (name, writer)
        broadcast(f"{name} joined the chat.", skip=connection)
        try:
            while line := reader.readline(MAX_LINE + 1):
                if len(line) > MAX_LINE:
                    writer.write(b"Message too long; disconnecting.\n")
                    writer.flush()
                    break
                message = line.decode("utf-8", errors="replace").strip()
                if message.lower() == "/quit":
                    break
                if message:
                    broadcast(f"{name}: {message}", skip=connection)
        finally:
            with clients_lock:
                clients.pop(connection, None)
            broadcast(f"{name} left the chat.", skip=connection)
            writer.close()
            reader.close()


def run_server() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Chat server listening on {HOST}:{PORT}")
        while True:
            connection, address = server.accept()
            threading.Thread(
                target=handle_client, args=(connection, address), daemon=True
            ).start()


def run_client(name: str) -> None:
    with socket.create_connection((HOST, PORT)) as connection:
        reader = connection.makefile("rb")
        connection.sendall((name[:40] + "\n").encode("utf-8"))

        def receive() -> None:
            for line in reader:
                print(line.decode("utf-8", errors="replace").rstrip())

        receiver = threading.Thread(target=receive, daemon=True)
        receiver.start()
        print("Type /quit to leave.")
        try:
            while True:
                message = input()
                connection.sendall((message + "\n").encode("utf-8"))
                if message.strip().lower() == "/quit":
                    break
        except EOFError:
            connection.sendall(b"/quit\n")
        receiver.join(timeout=1)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("server", "client"))
    parser.add_argument("--name", default="student", help="display name for client mode")
    args = parser.parse_args()
    if args.mode == "server":
        run_server()
    else:
        run_client(args.name)


if __name__ == "__main__":
    main()
