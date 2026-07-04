class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        minJumps = float('inf')
        dp = [None for i in range(n)]
        def dfs(i):
            nonlocal dp
            if i == n-1:
                # minJumps = min(minJumps, jumps)
                # return
                dp[i] = 0
                return 0


            if i >= n:
                return float('inf')

            if dp[i] != None:
                return dp[i]

            jumps = float('inf')
            for k in range(nums[i], 0, -1):
                jumps = min(jumps, 1+ dfs(i+k))

            dp[i] = jumps
            return jumps

        dfs(0)
        return dp[0]

            
        