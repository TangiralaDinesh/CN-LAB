# 16. Build a simple LAN in Cisco Packet Tracer

1. Place two PCs and one switch in a new Packet Tracer workspace.
2. Connect each PC to the switch with a copper straight-through cable.
3. Assign the PCs addresses in the same private subnet, for example:
   - PC0: `192.168.10.10`, mask `255.255.255.0`
   - PC1: `192.168.10.11`, mask `255.255.255.0`
4. Leave the default gateway empty because this LAN has no router.
5. Wait for the switch links to become active, then open PC0's command prompt
   and run `ping 192.168.10.11`.
6. Use **Simulation** mode and **Add Simple PDU** to observe ARP resolution and
   ICMP delivery. Record the topology and successful replies.

These are documentation-range addresses for a simulator, not addresses to
configure on a real network.
