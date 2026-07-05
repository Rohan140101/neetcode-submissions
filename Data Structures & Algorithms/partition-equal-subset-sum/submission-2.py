class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        arraySum = sum(nums)
        if arraySum % 2:
            return False

        target = arraySum // 2
        dp = [[None for i in range(target + 1)] for j in range(n)]
        def dfs(i, target):
            if i == n:
                return target == 0


            if dp[i][target] != None:
                return dp[i][target]


            case1, case2 = False, False
            if nums[i] <= target:
                case1 = dfs(i+1, target - nums[i])
            case2 = dfs(i+1, target)
            dp[i][target] = case1 or case2
            return dp[i][target]

        return dfs(0, target)

        