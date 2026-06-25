import heapq
from collections import deque
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        max_heap = []
        for num, count in counter.items():
            heapq.heappush(max_heap, (-count, num))

        output = []
        for i in range(k):
            count, num = heapq.heappop(max_heap)
            output.append(num)

        return output