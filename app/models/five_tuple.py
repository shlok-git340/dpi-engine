from dataclasses import dataclass


@dataclass(frozen=True)
class FiveTuple:
    src_ip: str
    dst_ip: str
    src_port: int
    dst_port: int
    protocol: str