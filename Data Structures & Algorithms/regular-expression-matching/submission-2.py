class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(s)
        n = len(p)
        dp = [[False for i in range(n + 1)] for j in range(m + 1)]
        vis = [[False for i in range(n + 1)] for j in range(m + 1)]
        def dfs(i, j):
            # print(i, j)
            if j == n:
                return i == m


            if vis[i][j]:
                return dp[i][j]

            vis[i][j] = True
            # else:
            #     return False

            # if i == m:
            #     return False

            match =  i < m and (s[i] == p[j] or p[j] == '.')
            if j + 1 < n and p[j+1] == "*":
                case1 = dfs(i, j+2) # not take case

                # Taking if letters match case
                case2 = False 
                if match:
                    case2 = dfs(i+1, j)

                dp[i][j] = case1 or case2
                return dp[i][j]
            
            if match:
                dp[i][j] = dfs(i+1, j+1)
                return dp[i][j]
            else:
                dp[i][j] = False
                return dp[i][j]


        return dfs(0, 0)


            
        