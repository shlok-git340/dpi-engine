from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Flow:
    packet_count: int = 0
    byte_count: int = 0

    sni: Optional[str] = None
    host: Optional[str] = None

    app_type: str = "UNKNOWN"

    blocked: bool = False