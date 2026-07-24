class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [None for i in range(n)]

        # def dfs(i):
        #     if i < 0:
        #         return 0

        #     if i == 0 or i == 1:
        #         return nums[i]

        #     if dp[i] != None:
        #         return dp[i]

        #     dp[i] = nums[i] + max(dfs(i-2), dfs(i-3))
        #     return dp[i]

        # return max(dfs(n-1), dfs(n-2))


        if(n <= 2):
            return max(nums)

        # dp[0] = nums[0]
        # dp[1] = nums[1]

        for i in range(n):
            # if i == 0 or i == 1:
                # dp[i] = nums[i]
                # continue
            ele1 = 0 if i-2 < 0 else dp[i-2]
            ele2 = 0 if i-3 < 0 else dp[i-3]

            dp[i] = nums[i] + max(ele1, ele2)

        return max(dp[n-1], dp[n-2])

        

        