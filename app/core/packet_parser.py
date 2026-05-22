from scapy.layers.inet import IP, TCP, UDP
from scapy.packet import Raw

from app.models.packet import ParsedPacket


class PacketParser:
    @staticmethod
    def parse(packet):
        if IP not in packet:
            return None

        ip = packet[IP]

        src_port = None
        dst_port = None
        protocol = "UNKNOWN"

        if TCP in packet:
            tcp = packet[TCP]
            src_port = tcp.sport
            dst_port = tcp.dport
            protocol = "TCP"

        elif UDP in packet:
            udp = packet[UDP]
            src_port = udp.sport
            dst_port = udp.dport
            protocol = "UDP"

        payload = b""

        if Raw in packet:
            payload = bytes(packet[Raw].load)

        return ParsedPacket(
            raw_packet=packet,
            src_ip=ip.src,
            dst_ip=ip.dst,
            src_port=src_port,
            dst_port=dst_port,
            protocol=protocol,
            payload=payload,
            length=len(packet)
        )