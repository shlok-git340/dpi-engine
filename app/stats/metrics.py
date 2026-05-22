from collections import defaultdict


class Metrics:
    def __init__(self):
        self.total_packets = 0
        self.forwarded = 0
        self.dropped = 0

        self.protocols = defaultdict(int)
        self.apps = defaultdict(int)

    def update(self, packet, flow, dropped=False):
        self.total_packets += 1

        self.protocols[packet.protocol] += 1
        self.apps[flow.app_type] += 1

        if dropped:
            self.dropped += 1
        else:
            self.forwarded += 1