# 1. Network commands and packet capture

The manual's command exercise covers interface configuration, hostname/DNS
lookups, routing, connectivity, and packet inspection. Commands differ by OS:

| Task | Linux/macOS | Windows |
|---|---|---|
| Show interface addresses | `ip addr` (`ifconfig` on older systems) | `ipconfig /all` |
| Show active connections | `ss -tunap` (`netstat -an` is portable) | `netstat -ano` |
| Resolve a name | `nslookup example.com` | `nslookup example.com` |
| Show a route | `traceroute example.com` (`tracepath` may be available) | `tracert example.com` |
| Test connectivity | `ping -c 4 127.0.0.1` | `ping -n 4 127.0.0.1` |
| Show ARP/neighbor cache | `ip neigh` (`arp -a`) | `arp -a` |
| Capture loopback traffic | `sudo tcpdump -i lo -n icmp` | Use Wireshark on the loopback adapter |

For a safe packet-capture exercise, capture a few pings to `127.0.0.1`, stop
the capture, and inspect the request/reply pair. Capturing on a shared or
public network may require permission. Do not add, delete, or alter ARP entries
for this observation exercise.
