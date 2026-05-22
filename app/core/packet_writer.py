from scapy.all import wrpcap


class PacketWriter:
    def __init__(self, path):
        self.path = path
        self.forwarded_packets = []

    def write(self, packet):
        self.forwarded_packets.append(packet)

    def save(self):
        wrpcap(self.path, self.forwarded_packets)