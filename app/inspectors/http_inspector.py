class HTTPInspector:
    @staticmethod
    def extract_host(payload: bytes):
        try:
            decoded = payload.decode(errors="ignore")

            lines = decoded.split("\r\n")

            for line in lines:
                if line.lower().startswith("host:"):
                    return line.split(":", 1)[1].strip()

        except Exception:
            return None

        return None