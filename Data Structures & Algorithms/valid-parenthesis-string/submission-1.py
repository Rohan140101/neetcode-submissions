class Solution:
    def checkValidString(self, s: str) -> bool:
        opened = 0
        n = len(s)
        vis = [[False for i in range(n+1)] for j in range(n+1)]
        dp = [[False for i in range(n+1)] for j in range(n+1)]
        def checker(i, opened):
            # print(i, opened, n)
            if vis[i][opened]:
                return dp[i][opened]


            vis[i][opened] = True
            if i == n:
                if not opened:
                    dp[i][opened] = True
                    # return
                else:
                    dp[i][opened] = False
                    # return False
                return dp[i][opened]
            first_char = s[i]
            if first_char == "(":
                opened += 1
                return checker(i+1, opened)
            elif first_char == ")":
                if opened:
                    opened -= 1
                    return checker(i+1, opened)
                else:
                    return False 
            else:
                ## Case 1 - Consider "("
                case1 = checker(i+1, opened + 1)



                ## Case 2 - Consider ")"
                case2 = False
                if opened:
                    case2 = checker(i+1, opened - 1)

                ## Case 3 - Consider ""
                case3 = checker(i+1, opened)

                return case1 or case2 or case3

        return checker(0, 0)
        