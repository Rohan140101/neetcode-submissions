class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False for i in range(n+1)] for j in range(m+1)]
        vis = [[False for i in range(n+1)] for j in range(m+1)]
        def recur(i, j):
            if vis[i][j]:
                return dp[i][j]

            vis[i][j] = True

            if j == n:
                return i == m

            


            if j + 1 < n and p[j+1] == "*":
                # Case 1 - Take
                if i == m:
                    return recur(i, j+2)


                case1 = False
                case2 = False
                if p[j] == s[i] or p[j] == ".":
                    case1 = recur(i+1, j)
                    case2 = recur(i, j+2)
                    return case1 or case2
                else:
                    # Case 2 - Ignore
                    return recur(i, j+2)

                

            elif p[j] == ".":
                return recur(i+1, j+1)


            elif i < m and p[j] == s[i]:
                return recur(i+1, j+1)


            return False
    
        return recur(0, 0)