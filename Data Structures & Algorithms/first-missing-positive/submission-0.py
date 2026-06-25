class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] > 1:
            return 1
        for i in range(1, len(nums)):
            if nums[i] <= 1:
                continue


            if i > 0 and nums[i] == nums[i - 1] + 1:
                continue

            return max(nums[i-1] + 1, 1)

        return max(1, nums[-1] + 1)
        