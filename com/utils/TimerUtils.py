import time


class TimerUtils:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.perf_counter()
        self.execution_time = self.end_time - self.start_time
        print(f"Execution time using context manager: {self.execution_time} seconds")
