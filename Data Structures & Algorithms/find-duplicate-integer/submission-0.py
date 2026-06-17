class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            if counts[num] == 2:
                return num
        