from dataclasses import dataclass
from typing import Optional


@dataclass
class ParsedPacket:
    raw_packet: object

    src_ip: str
    dst_ip: str

    src_port: Optional[int]
    dst_port: Optional[int]

    protocol: str

    payload: bytes

    length: int