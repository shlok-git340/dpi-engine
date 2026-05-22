from scapy.layers.dns import DNSQR


class DNSInspector:
    @staticmethod
    def extract_query(packet):
        try:
            if packet.haslayer(DNSQR):
                return packet[DNSQR].qname.decode()
        except Exception:
            return None

        return None