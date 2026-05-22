from app.models.flow import Flow
from app.models.five_tuple import FiveTuple



class FlowTracker:
    def __init__(self):
        self.flows = {}

    def get_flow(self, packet):
        key = FiveTuple(
            src_ip=packet.src_ip,
            dst_ip=packet.dst_ip,
            src_port=packet.src_port or 0,
            dst_port=packet.dst_port or 0,
            protocol=packet.protocol
        )

        if key not in self.flows:
            self.flows[key] = Flow()

        flow = self.flows[key]

        flow.packet_count += 1
        flow.byte_count += packet.length

        return flow