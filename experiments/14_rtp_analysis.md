# 14. RTP delay and loss analysis

Use a provided lab capture or capture a VoIP/streaming session that you own or
are authorized to analyze. Do not record other people's calls.

1. Open the capture in Wireshark and identify RTP packets with the `rtp`
   display filter. If Wireshark does not recognize the stream, select a packet
   and use **Analyze → Decode As…** only when the lab instructions identify
   the RTP ports.
2. Open **Telephony → RTP → RTP Streams**, select the relevant stream, and
   choose **Analyze**.
3. Record the packet count, sequence-number gaps, packet loss, jitter, and
   out-of-order packets shown in the analysis.
4. Use **Telephony → RTP → RTP Stream Analysis** to view sequence number,
   timestamp, delta, and jitter. Compare the direction of each stream
   separately.
5. Save the capture only if permitted, and include the stream selection and
   observed measurements in the lab record.

RTP sequence numbers reveal missing or reordered packets; timestamps and
inter-arrival measurements help estimate jitter. A capture made at one host
cannot establish end-to-end network delay on its own, and observed loss may
also be caused by capture drops.
