from threading import Timer

class clock():
    def __init__(self, frequency, timeoutEvent, limit = None):  # timeout in seconds
        self.time = 1 / frequency
        self.event = timeoutEvent
        self.count = 0
        self.limit = limit
        self.timer = Timer(self.time, self.timeout)
        self.timer.start()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.timer.cancel()

    def timeout(self):
        self.reset()
        self.event()
        if not self.limit is None:
            self.count += 1
            print('incrementing clock')
            if self.count >= self.limit:
                self.stop()

    def reset(self):
        self.timer.cancel()
        self.timer = Timer(self.time, self.timeout)
        self.timer.start()

    def stop(self):
        print('stopping clock')
        self.timer.cancel()