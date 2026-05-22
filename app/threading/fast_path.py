import threading


class FastPath(threading.Thread):
    def __init__(self, input_queue, engine):
        super().__init__()

        self.input_queue = input_queue
        self.engine = engine

    def run(self):
        while True:
            packet = self.input_queue.pop()
            self.engine.process(packet)