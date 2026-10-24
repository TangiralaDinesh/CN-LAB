"""Demonstrate ARP and RARP lookups using a simulated mapping table."""

import ipaddress
import re

ARP_TABLE = {
    "192.168.1.1": "00:0a:95:9d:68:16",
    "192.168.1.2": "00:0a:95:9d:68:17",
    "192.168.1.3": "00:0a:95:9d:68:18",
}
MAC_PATTERN = re.compile(r"(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}\Z")


def lookup_ip(ip_address: str) -> str | None:
    normalized_ip = str(ipaddress.IPv4Address(ip_address))
    return ARP_TABLE.get(normalized_ip)


def lookup_mac(mac_address: str) -> str | None:
    if not MAC_PATTERN.fullmatch(mac_address):
        raise ValueError("MAC address must use the format 00:11:22:33:44:55")
    reverse_table = {mac.lower(): ip for ip, mac in ARP_TABLE.items()}
    return reverse_table.get(mac_address.lower())


def main() -> None:
    print("ARP/RARP table:")
    for ip, mac in ARP_TABLE.items():
        print(f"  {ip:15} <-> {mac}")
    while True:
        mode = input("Choose arp, rarp, or quit: ").strip().lower()
        if mode in ("quit", "q"):
            break
        if mode == "arp":
            address = input("IPv4 address: ").strip()
            try:
                result = lookup_ip(address)
            except ipaddress.AddressValueError as error:
                print(f"Invalid IPv4 address: {error}")
                continue
            print(f"ARP reply: {address} is at {result}" if result else "No table entry found.")
        elif mode == "rarp":
            address = input("MAC address: ").strip()
            try:
                result = lookup_mac(address)
            except ValueError as error:
                print(error)
                continue
            print(f"RARP reply: {address} maps to {result}" if result else "No table entry found.")
        else:
            print("Enter arp, rarp, or quit.")


if __name__ == "__main__":
    main()
