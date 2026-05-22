from app.rules.blocklist import (
    BLOCKED_APPS,
    BLOCKED_DOMAINS,
    BLOCKED_IPS
)


class RuleManager:
    @staticmethod
    def is_blocked(packet, flow):
        if packet.src_ip in BLOCKED_IPS:
            return True

        if flow.app_type in BLOCKED_APPS:
            return True

        if flow.sni:
            for domain in BLOCKED_DOMAINS:
                if domain in flow.sni:
                    return True

        return False