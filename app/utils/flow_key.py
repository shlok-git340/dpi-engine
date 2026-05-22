def make_flow_key(packet):
    endpoints = sorted([
        (packet.src_ip, packet.src_port),
        (packet.dst_ip, packet.dst_port)
    ])

    return (
        endpoints[0],
        endpoints[1],
        packet.protocol
    )