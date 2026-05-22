import numpy as np


def build_features(flow):
    return np.array([
        flow.packet_count,
        flow.byte_count,
        int(flow.blocked)
    ]).reshape(1, -1)
