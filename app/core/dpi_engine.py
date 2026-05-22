from app.core.packet_parser import PacketParser
from app.core.flow_tracker import FlowTracker
from app.inspectors.tls_inspector import TLSInspector
from app.inspectors.http_inspector import HTTPInspector
from app.inspectors.app_classifier import AppClassifier
from app.rules.rule_manager import RuleManager
from app.stats.metrics import Metrics
from app.core.tcp_reassembler import TCPReassembler
# from app.ml.anomaly_detector import AnomalyDetector
# from app.ml.feature_engineering import build_features


class DPIEngine:
    def __init__(self, writer=None):
        self.flow_tracker = FlowTracker()
        self.metrics = Metrics()
        self.reassembler = TCPReassembler()
        self.writer = writer
        # self.detector = AnomalyDetector()

    def process(self, raw_packet):
        packet = PacketParser.parse(raw_packet)

        if not packet:
            return

        flow = self.flow_tracker.get_flow(packet)
        existing_flow = self.flow_tracker.get_flow(packet)

        if existing_flow and existing_flow.app_type != "UNKNOWN":
            packet.app_type = existing_flow.app_type

        if (
            packet.dst_port == 443
            or packet.src_port == 443
        ):

            stream_data = self.reassembler.add_packet(packet)

            if not stream_data:
                return

            print(
                "STREAM SIZE:",
                len(stream_data)
            )
            if len(packet.payload) < 20:
                return

            # Wait until enough TLS data accumulates
            if len(stream_data) < 150:
                return

            sni = TLSInspector.extract_sni(stream_data)

            if sni:
                print("SNI DETECTED:", sni)

                flow.sni = sni

                flow.app_type = AppClassifier.classify(sni)

                # Clear stream after successful parse
                self.reassembler.clear_stream(packet)

        elif packet.dst_port == 80:
            host = HTTPInspector.extract_host(packet.payload)

            if host:
                flow.host = host
                flow.app_type = AppClassifier.classify(host)

        blocked = RuleManager.is_blocked(packet, flow)

        flow.blocked = blocked

        self.metrics.update(packet, flow, blocked)
        print(
            packet.protocol,
            packet.src_ip,
            "->",
            packet.dst_ip,
            flow.app_type,
            "BLOCKED" if blocked else "ALLOWED"
        )
        # features = build_features(flow)

        # prediction = self.detector.predict(features)

        # if prediction[0] == -1:
        #     print("ANOMALY DETECTED")

        if not blocked and self.writer:
            self.writer.write(raw_packet)