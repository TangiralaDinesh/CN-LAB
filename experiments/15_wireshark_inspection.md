# 15. Inspect packets with Wireshark

1. Start Wireshark and choose your own loopback or lab interface.
2. Begin a short capture, then generate a small amount of authorized test
   traffic (for example, ping `127.0.0.1`).
3. Stop the capture. Inspect the packet list and expand **Frame**, **Ethernet
   II**, **Internet Protocol**, and the transport/application layer where
   present.
4. Select a TCP packet and use **Follow → TCP Stream** to view that
   conversation. Do not follow or save conversations containing private data.
5. Use **Statistics → Protocol Hierarchy** and **Statistics → Conversations**
   to summarize the capture.
6. Record the interface, filters, packet types, and observations. Close or
   remove captures that contain information you should not retain.

For a command-line alternative on Linux, `sudo tcpdump -i lo -n icmp` displays
only ICMP on loopback. Stop it with Ctrl+C.
