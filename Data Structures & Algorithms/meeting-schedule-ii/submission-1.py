"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        interval_list = []
        for interval in intervals:
            interval_list.append([interval.start, interval.end])

        interval_list = sorted(interval_list, key = lambda x: x[0])
        
        # rooms = 0
        room_end_times = []
        for interval in interval_list:
            if len(room_end_times) < 1:
                room_end_times.append(interval[1])
                continue
            
            min_end_time = min(room_end_times)
            if interval[0] >= min_end_time:
                min_end_time_idx = room_end_times.index(min_end_time)
                room_end_times[min_end_time_idx] = interval[1]
            else:
                room_end_times.append(interval[1])
        
        return len(room_end_times)