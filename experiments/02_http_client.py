"""Fetch one HTTP/1.1 response using a raw TCP socket."""

import argparse
import socket
import sys
from urllib.parse import quote, urlsplit


def fetch(url: str, timeout: float = 10.0) -> bytes:
    parsed = urlsplit(url)
    if parsed.scheme != "http" or not parsed.hostname:
        raise ValueError("provide an http:// URL (HTTPS is not handled by this socket example)")
    if parsed.username or parsed.password:
        raise ValueError("URLs containing credentials are not supported")

    host = parsed.hostname.encode("idna").decode("ascii")
    port = parsed.port or 80
    path = quote(parsed.path or "/", safe="/%:@!$&'()*+,;=-._~")
    if parsed.query:
        query = quote(parsed.query, safe="/%?:@!$&'()*+,;=-._~")
        path += f"?{query}"
    host_header = f"[{host}]" if ":" in host else host
    if port != 80:
        host_header += f":{port}"

    request = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {host_header}\r\n"
        "User-Agent: CN-LAB/1.0\r\n"
        "Accept: */*\r\n"
        "Connection: close\r\n\r\n"
    ).encode("ascii")

    chunks = []
    with socket.create_connection((host, port), timeout=timeout) as connection:
        connection.sendall(request)
        while chunk := connection.recv(4096):
            chunks.append(chunk)
    return b"".join(chunks)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="HTTP URL, for example http://example.com/")
    args = parser.parse_args()

    try:
        sys.stdout.buffer.write(fetch(args.url))
    except (OSError, ValueError) as error:
        print(f"HTTP client error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
