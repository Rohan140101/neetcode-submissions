class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Recursion
        # answer = float('inf')
        # dp = [None for i in range(amount + 1)]
        # dp[0] = 0

        # def dfs(amount, coins):
        #     if amount < 0:
        #         return float('inf')

        #     if dp[amount] is not None:
        #         return dp[amount]


        #     minCoins = float('inf')
        #     for coin in coins:
        #         minCoins = min(minCoins, 1 + dfs(amount - coin, coins))

        #     dp[amount] = minCoins
        #     return minCoins

        # answer = dfs(amount, coins)
        # if answer == float('inf'):
        #     return -1
        # return answer

        # DP
        dp = [-1 for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            minCoins = float('inf')
            for coin in coins:
                diff = i - coin
                if diff >= 0:
                    minCoins = min(minCoins, 1 + dp[diff])

            dp[i] = minCoins


        return dp[-1] if dp[-1] != float('inf') else -1


 

        