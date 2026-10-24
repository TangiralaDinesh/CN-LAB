# Experiment index

This folder follows the numbering in the two notebook photographs, not the
numbering in the PDF manual. PDF page numbers below refer to the printed page
numbers in the manual.

| Notebook | Experiment | Manual section |
|---:|---|---|
| 1 | Network commands and packet capture | pp. 4–13 |
| 2 | HTTP web client using TCP sockets | pp. 18–23 |
| 3 | Local DNS server host name and IP address | pp. 80–84 |
| 4 | TCP echo client and server | pp. 24–29 |
| 5 | Multi-client TCP chat | pp. 30–37 |
| 6 | TCP file transfer | pp. 38–43 |
| 7 | ARP/RARP simulation | pp. 44–49 |
| 8 | TCP and UDP performance with NS2 | pp. 61–66 |
| 9 | Distance-vector routing with NS2 | pp. 67–72 |
| 10 | Link-state routing with NS2 | pp. 73–79 |
| 11 | Local DNS server host name and IP address (repeat) | pp. 80–84 |
| 12 | CRC error detection | pp. 85–90 |
| 13 | Wireshark capture/display filters | pp. 91–95 |
| 14 | RTP delay and loss analysis | pp. 96–101 |
| 15 | Inspecting packets with Wireshark | pp. 102–105 |
| 16 | Simple LAN in Cisco Packet Tracer | pp. 106–109 |
| 17 | Topologies with the Benchmark LAN Trainer Kit | pp. 110–114 |

The notebook lists the local DNS-server exercise at both 3 and 11. Both entries
use `11_dns_server_info.py`; the manual's DNS-server section (pp. 80–84) prints
the local machine hostname/address rather than the configured resolver, so the
script reports configured resolver IPs and reverse-resolved names instead.
The manual's separate local-machine hostname exercise (pp. 14–17) is not a
separate entry in the notebook index.

## Run the Python examples

Use Python 3.10 or newer; no third-party packages are required.

```text
python experiments/02_http_client.py http://example.com/
python experiments/04_echo_server.py
python experiments/04_echo_client.py
python experiments/05_chat.py server
python experiments/05_chat.py client --name Alice
python experiments/06_file_server.py
python experiments/06_file_client.py path/to/file.txt
python experiments/07_arp_rarp.py
python experiments/11_dns_server_info.py
python experiments/12_crc.py
```

Run each server in one terminal and its client in a second terminal. The socket
examples use the loopback interface, so they do not expose a service to the
network. The HTTP client contacts the URL you provide.

## Run the NS2 examples

With NS2 and (optionally) NAM installed, run a script from a writable working
directory, for example:

```text
ns experiments/08_tcp_udp.tcl
```

Each script writes a trace and NAM file in the current directory. NS2 builds
differ, and `rtproto LS` may not be available in every package; the link-state
example uses the protocol command shown in the supplied manual.

Experiments 1 and 13–17 are operational lab exercises rather than standalone
programs. Their files give safe, repeatable steps; capture or inspect only
traffic and networks you own or are authorized to use.
