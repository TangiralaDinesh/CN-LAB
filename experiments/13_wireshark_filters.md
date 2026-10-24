# 13. Wireshark filter expressions

Capture only traffic you are authorized to inspect. A capture filter limits
what is recorded; a display filter only limits what is shown from the capture.

## Capture filters (BPF syntax)

| Purpose | Filter |
|---|---|
| ICMP ping packets | `icmp` |
| DNS traffic | `udp port 53` |
| TCP traffic to/from port 80 | `tcp port 80` |
| Traffic to/from one host | `host 192.0.2.10` |
| Local loopback pings | `host 127.0.0.1 and icmp` |

## Display filters

| Purpose | Filter |
|---|---|
| ICMP packets | `icmp` |
| DNS queries and responses | `dns` |
| TCP packets | `tcp` |
| SYN packets | `tcp.flags.syn == 1` |
| Retransmissions | `tcp.analysis.retransmission` |
| RTP packets | `rtp` |
| Traffic to/from one address | `ip.addr == 192.0.2.10` |

Replace documentation addresses such as `192.0.2.10` with an address from your
own authorized lab. In Wireshark, enter a capture filter before starting a
capture; enter a display filter after capture. Use **Apply** to check a display
filter and **Clear** to restore the full packet list.
