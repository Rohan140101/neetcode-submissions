class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums.sort()
        # if nums[0] > 1:
        #     return 1
        # n = len(nums)
        # i = 0
        # while i < n:
        #     if i > 0 and nums[i] == nums[i-1]:
        #         i += 1
        #         continue

        #     if nums[i] <= 1:
        #         i += 1
        #         continue


        #     if i > 0 and nums[i] == nums[i - 1] + 1:
        #         i += 1
        #         continue

        #     return max(nums[i-1] + 1, 1)

        # return max(1, nums[-1] + 1)

        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            abs_value = abs(nums[i])
            if abs_value > n:
                continue
            if nums[abs_value - 1] > 0:
                nums[abs_value - 1] *= -1

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
        