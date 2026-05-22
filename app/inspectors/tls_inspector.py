import struct


class TLSInspector:
    @staticmethod
    def extract_sni(payload: bytes):
        try:
            # TLS Handshake
            if len(payload) < 5:
                return None

            # Content Type must be Handshake (22)
            if payload[0] != 22:
                return None

            # Handshake Type must be Client Hello (1)
            if payload[5] != 1:
                return None

            offset = 43

            # Session ID
            session_id_length = payload[offset]
            offset += 1 + session_id_length

            # Cipher Suites
            cipher_suites_length = struct.unpack(
                "!H",
                payload[offset:offset + 2]
            )[0]

            offset += 2 + cipher_suites_length

            # Compression Methods
            compression_methods_length = payload[offset]
            offset += 1 + compression_methods_length

            # Extensions Length
            extensions_length = struct.unpack(
                "!H",
                payload[offset:offset + 2]
            )[0]

            offset += 2

            end = offset + extensions_length

            while offset + 4 <= end:
                extension_type = struct.unpack(
                    "!H",
                    payload[offset:offset + 2]
                )[0]

                extension_length = struct.unpack(
                    "!H",
                    payload[offset + 2:offset + 4]
                )[0]

                offset += 4

                # SNI Extension
                if extension_type == 0:
                    sni_list_length = struct.unpack(
                        "!H",
                        payload[offset:offset + 2]
                    )[0]

                    offset += 2

                    sni_type = payload[offset]

                    offset += 1

                    sni_length = struct.unpack(
                        "!H",
                        payload[offset:offset + 2]
                    )[0]

                    offset += 2

                    server_name = payload[
                        offset:offset + sni_length
                    ].decode()

                    return server_name

                offset += extension_length

        except Exception:
            return None

        return None