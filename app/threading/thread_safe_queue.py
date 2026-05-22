from queue import Queue


class ThreadSafeQueue:
    def __init__(self):
        self.queue = Queue()

    def push(self, item):
        self.queue.put(item)

    def pop(self):
        return self.queue.get()