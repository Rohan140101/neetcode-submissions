class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # # Memoization
        # m = len(word1)
        # n = len(word2)
    
        # dp = [[None for i in range(n)] for j in range(m)]
        # def f(i, j):
        #     print(i, j)
        #     if i < 0:
        #         return j + 1
            
        #     if j < 0:
        #         return i + 1

        #     if dp[i][j] != None:
        #         return dp[i][j]

        #     if word1[i] == word2[j]:
        #         dp[i][j] = f(i-1, j-1)
        #     else:
        #         dp[i][j] = 1 + min(f(i-1, j), f(i, j-1), f(i-1, j-1))

        #     return dp[i][j]
        # return f(m-1, n-1)


        # Tabulation
        m = len(word1)
        n = len(word2)
    
        dp = [[None for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i

        for j in range(n+1):
            dp[0][j] = j

        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        return dp[m][n]


        