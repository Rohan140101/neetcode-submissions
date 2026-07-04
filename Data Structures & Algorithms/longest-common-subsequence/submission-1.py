class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # m = len(text1)
        # n = len(text2)

        # dp = [[None for i in range(n)] for j in range(m)]

        # def dfs(i, j):
        #     if i < 0 or j < 0:
        #         return 0

        #     if dp[i][j] != None:
        #         return dp[i][j]

        #     if text1[i] == text2[j]:
        #         dp[i][j] = 1 + dfs(i-1, j-1)
        #     else:
        #         dp[i][j] = max(dfs(i-1, j), dfs(i, j-1))

        #     return dp[i][j]

        # dfs(m-1, n-1)
        # return dp[m-1][n-1]

        # Tabulation

        m = len(text1)
        n = len(text2)

        dp = [[None for i in range(n+1)] for j in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 0

        for j in range(n+1):
            dp[0][j] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]

            
        
        