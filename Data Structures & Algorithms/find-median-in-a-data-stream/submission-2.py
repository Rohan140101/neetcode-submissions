from collections import defaultdict
import heapq
class MedianFinder:

    def __init__(self):
        self.data_stream_counts = defaultdict(int)
        self.count = 0
        

    def addNum(self, num: int) -> None:
        self.data_stream_counts[num] += 1
        self.count += 1

    def findMedian(self) -> float:
        # self.data_stream.sort()
        # length = len(self.data_stream)
        # if length % 2:
        #     # print(length, self.data_stream)
        #     return self.data_stream[length//2]
        # else:
        #     return (self.data_stream[length//2 - 1] + self.data_stream[length//2] ) /2
        min_heap = [(k, v) for (k, v) in self.data_stream_counts.items()]
        heapq.heapify(min_heap)
        if self.count % 2:
            index = self.count // 2
            ans = None
            while min_heap and index >= 0:
                key, val = heapq.heappop(min_heap)
                ans = key
                index = index - val

            return  ans
        else:
            index = self.count // 2 - 1
            num1 = None
            while min_heap and index >= 0:
                key, val = heapq.heappop(min_heap)
                num1 = key
                index = index - val
            
            if index < -1:
                num2 = num1
            elif index == -1:
                key, val = heapq.heappop(min_heap)
                num2 = key

            return (num1 + num2) / 2




        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()