class MedianFinder:

    def __init__(self):
        self.data_stream = []
        

    def addNum(self, num: int) -> None:
        self.data_stream.append(num)

    def findMedian(self) -> float:
        self.data_stream.sort()
        length = len(self.data_stream)
        if length % 2:
            # print(length, self.data_stream)
            return self.data_stream[length//2]
        else:
            return (self.data_stream[length//2 - 1] + self.data_stream[length//2] ) /2



        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()