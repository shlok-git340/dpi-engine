import threading


class LoadBalancer(threading.Thread):
    def __init__(self, input_queue, workers):
        super().__init__()

        self.input_queue = input_queue
        self.workers = workers

    def run(self):
        while True:
            packet = self.input_queue.pop()

            index = hash(packet.src_ip) % len(self.workers)

            self.workers[index].input_queue.push(packet)