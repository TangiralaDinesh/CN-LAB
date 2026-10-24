"""Send one file to the local TCP file server."""

import argparse
import socket
import sys
from pathlib import Path

HOST = "127.0.0.1"
PORT = 65434
MAX_FILE_SIZE = 10 * 1024 * 1024


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    source = args.file
    if not source.is_file():
        print(f"Not a regular file: {source}", file=sys.stderr)
        return 1
    size = source.stat().st_size
    if size > MAX_FILE_SIZE:
        print(f"File exceeds the {MAX_FILE_SIZE}-byte limit.", file=sys.stderr)
        return 1

    header = f"{source.name}|{size}\n".encode("utf-8")
    with socket.create_connection((HOST, PORT)) as connection, source.open("rb") as file:
        connection.sendall(header)
        while chunk := file.read(65536):
            connection.sendall(chunk)
    print(f"Sent {source.name!r} ({size} bytes).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
