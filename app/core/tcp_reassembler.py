from collections import defaultdict


class TCPReassembler:
    def __init__(self):
        self.streams = defaultdict(bytes)

    def _make_key(self, packet):
        """
        Create direction-independent TCP stream key.
        """

        endpoints = sorted([
            (packet.src_ip, packet.src_port),
            (packet.dst_ip, packet.dst_port)
        ])

        return (
            endpoints[0],
            endpoints[1],
            packet.protocol
        )

    def add_packet(self, packet):
        if not packet.payload:
            return None

        key = self._make_key(packet)

        self.streams[key] += packet.payload

        return self.streams[key]

    def clear_stream(self, packet):
        key = self._make_key(packet)

        if key in self.streams:
            del self.streams[key]