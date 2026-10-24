"""Receive one file over a local TCP connection."""

import socket
from pathlib import Path

HOST = "127.0.0.1"
PORT = 65434
MAX_FILE_SIZE = 10 * 1024 * 1024
OUTPUT_DIR = Path(__file__).resolve().parent / "received_files"


def receive_file(connection: socket.socket) -> Path:
    reader = connection.makefile("rb")
    header = reader.readline(512)
    try:
        name_bytes, size_bytes = header.rstrip(b"\n").rsplit(b"|", 1)
        name = name_bytes.decode("utf-8")
        size = int(size_bytes)
    except (ValueError, UnicodeDecodeError) as error:
        raise ValueError("invalid file-transfer header") from error
    if not name or Path(name).name != name or name in (".", ".."):
        raise ValueError("filename must be a plain basename")
    if not 0 <= size <= MAX_FILE_SIZE:
        raise ValueError(f"file size must be between 0 and {MAX_FILE_SIZE} bytes")

    OUTPUT_DIR.mkdir(exist_ok=True)
    destination = OUTPUT_DIR / name
    remaining = size
    created = False
    complete = False
    try:
        with destination.open("xb") as output:
            created = True
            while remaining:
                chunk = reader.read(min(65536, remaining))
                if not chunk:
                    raise ConnectionError("client disconnected before the file was complete")
                output.write(chunk)
                remaining -= len(chunk)
        complete = True
    finally:
        if created and not complete:
            destination.unlink(missing_ok=True)
    return destination


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"File server listening on {HOST}:{PORT}")
        connection, address = server.accept()
        with connection:
            print(f"Connected by {address}")
            saved = receive_file(connection)
            print(f"Saved {saved.name!r} ({saved.stat().st_size} bytes) to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
