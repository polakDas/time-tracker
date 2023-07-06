import time

class TimeTracker:
    def __init__(self):
        self.start_time = 0
        self.current_time = 0
        self.total_time = 0

    def start_tracker(self):
        if not self.start_time:
            self.start_time = time.time()
            print(self.start_time)

    def pause_tracker(self):
        print(self.start_time)
        if self.start_time:
            self.current_time = time.time()
            self.total_time += (self.current_time - self.start_time) // 60
            self.start_time = 0
            print(self.total_time)
        print("Not working pause")

    def stop_tracker(self):
        self.current_time = time.time()
        if self.start_time:
            self.total_time += (self.current_time - self.start_time) // 60
            print(self.total_time)
        print("not working stop")
