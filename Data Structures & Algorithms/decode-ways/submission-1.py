class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [None for i in range(n)]
        def dfs(i):
            if i == -1:
                return 1

            if dp[i] != None:
                return dp[i]


            branch1 = 0
            branch2 = 0

            if s[i] != "0":
                branch1 = dfs(i-1)

            if i > 0 and s[i-1] != "0":
                one_before = int(s[i-1:i+1])
                if one_before <= 26:
                    branch2 = dfs(i-2)

            dp[i] = branch1 + branch2
            return dp[i]

        return dfs(n - 1)        