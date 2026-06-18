from collections import defaultdict, deque

class TimeMap:
    def __init__(self):
        # self.store = defaultdict(lambda: defaultdict(int))
        self.store = defaultdict(lambda: deque([]))

    def set(self, key: str, value: str, timestamp: int) -> None:
        # self.store[key][timestamp] = value
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # if key in self.store:
        #     sorted_ts_values = {k: v for (k, v) in sorted(self.store[key].items(), key=lambda x: x[0])}
        #     prev_val = ""
        #     for ts, val in sorted_ts_values.items():
        #         if ts > timestamp:
        #             break
        #         prev_val = val
        #     return prev_val
        # return ""

        if key in self.store:
            queue = self.store[key]
            prev_val = ""
            for ts, val in queue:
                if ts > timestamp:
                    break
                prev_val = val
            return prev_val

        return ""