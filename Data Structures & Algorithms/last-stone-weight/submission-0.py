import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            val = abs(stone1 - stone2)
            if val > 0:
                heapq.heappush(heap, -val)

        if heap:
            return -heap[0]
        
        return 0
        