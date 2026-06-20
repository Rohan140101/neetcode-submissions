from collections import defaultdict
import heapq
class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []
        

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)

        if len(self.left) > len(self.right) + 1:
            val = heapq.heappop(self.left)
            heapq.heappush(self.right, -val)
        
        if len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)
 
    def findMedian(self) -> float:
        # self.data_stream.sort()
        # length = len(self.data_stream)
        # if length % 2:
        #     # print(length, self.data_stream)
        #     return self.data_stream[length//2]
        # else:
        #     return (self.data_stream[length//2 - 1] + self.data_stream[length//2] ) /2
        # print(self.left, self.right)
        totalCount = len(self.left) + len(self.right)
        if totalCount % 2:
            if len(self.left) > len(self.right):
                return -self.left[0]
            else:
                return self.right[0]

        else:
            num1 = self.left[0]
            num2 = self.right[0]
            return (-num1 + num2) / 2





        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()