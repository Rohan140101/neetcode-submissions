class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [[-1 for i in range(n+1)] for j in range(n)]

        def recur(i, prev_i):
            if i == n:
                return 0
                
            if dp[i][prev_i + 1] != -1:
                return dp[i][prev_i + 1]

            notTake = 0 + recur(i+1, prev_i)
            length = notTake
            if prev_i == -1 or nums[i] > nums[prev_i]:
                take = 1 + recur(i+1, i)
                length = max(notTake, take)

            dp[i][prev_i + 1] = length
            return length

        return recur(0, -1)
                

            

            


                
            
        