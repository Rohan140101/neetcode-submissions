class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # answers = set()
        # n = len(nums)
        # for i in range(n - 2):
        #     for j in range(i+1, n - 1):
        #         for k in range(j+1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 curSet = [nums[i], nums[j], nums[k]]
        #                 curSet.sort()
        #                 answers.add(tuple(curSet))
        # return [list(x) for x in answers]

        answers = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue                
            j = i + 1
            k = n - 1
            while j < k:
                value = nums[i] + nums[j] + nums[k]
                if value == 0:
                    answers.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif value < 0:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1



        return answers
        