import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]
        nums = [-x for x in nums]
        heapq.heapify(nums)
        
        return_Val = None
        for i in range(k):
            return_Val = heapq.heappop(nums)
        return -return_Val
        