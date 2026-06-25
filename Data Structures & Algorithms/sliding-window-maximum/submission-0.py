class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        l = 0
        r = k
        n = len(nums)
        while r <= n:
            windowMax = max(nums[l:r])
            answer.append(windowMax)
            l += 1
            r += 1

        return answer

        