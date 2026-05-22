from sqlalchemy import Column, Integer, String, Boolean

from app.database.connection import Base


class FlowRecord(Base):
    __tablename__ = "flows"

    id = Column(Integer, primary_key=True)

    src_ip = Column(String)
    dst_ip = Column(String)

    protocol = Column(String)

    app_type = Column(String)

    packet_count = Column(Integer)
    byte_count = Column(Integer)

    blocked = Column(Boolean)