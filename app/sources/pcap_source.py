from scapy.all import rdpcap


class PcapSource:
    def __init__(self, path):
        self.path = path

    def packets(self):
        packets = rdpcap(self.path)

        for packet in packets:
            yield packet