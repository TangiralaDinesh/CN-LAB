"""Show configured DNS resolver addresses and reverse-resolved names."""

import ipaddress
import socket
import sys
from pathlib import Path

RESOLV_CONF = Path("/etc/resolv.conf")


def configured_resolvers() -> list[str]:
    if not RESOLV_CONF.is_file():
        raise FileNotFoundError(
            f"{RESOLV_CONF} is unavailable; on Windows, inspect 'ipconfig /all' "
            "to find configured DNS servers."
        )
    addresses = []
    for line in RESOLV_CONF.read_text(encoding="utf-8").splitlines():
        fields = line.split("#", 1)[0].split()
        if len(fields) >= 2 and fields[0] == "nameserver":
            try:
                addresses.append(str(ipaddress.ip_address(fields[1])))
            except ValueError as error:
                raise ValueError(f"invalid nameserver address {fields[1]!r}") from error
    return list(dict.fromkeys(addresses))


def main() -> int:
    try:
        addresses = configured_resolvers()
    except (OSError, ValueError) as error:
        print(f"Could not read resolver configuration: {error}", file=sys.stderr)
        return 1
    if not addresses:
        print("No DNS resolver addresses were found in /etc/resolv.conf.", file=sys.stderr)
        return 1

    for address in addresses:
        try:
            hostname = socket.gethostbyaddr(address)[0]
        except (socket.herror, socket.gaierror):
            hostname = "(no reverse-DNS hostname available)"
        print(f"DNS server IP: {address}")
        print(f"DNS server host name: {hostname}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
