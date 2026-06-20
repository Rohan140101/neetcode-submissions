import heapq
class MedianFinder:

    def __init__(self):
        self.data_stream = []
        

    def addNum(self, num: int) -> None:
        self.data_stream.append(num)

    def findMedian(self) -> float:
        # self.data_stream.sort()
        # length = len(self.data_stream)
        # if length % 2:
        #     # print(length, self.data_stream)
        #     return self.data_stream[length//2]
        # else:
        #     return (self.data_stream[length//2 - 1] + self.data_stream[length//2] ) /2
        min_heap = self.data_stream.copy()
        heapq.heapify(min_heap)

        length = len(min_heap)
        # print(length)
        if length % 2:
            index = length // 2
            for i in range(index):
                heapq.heappop(min_heap)
            answer = heapq.heappop(min_heap)

            return answer
        else:
            index = length // 2 - 1
            for i in range(index):
                heapq.heappop(min_heap)
            num1 = heapq.heappop(min_heap)
            num2 = heapq.heappop(min_heap)
            # print(num1, num2)
            return (num1 + num2) / 2


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()