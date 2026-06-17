class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        def dfs(prices, i, n, profit, buyFlag, sellFlag):
            if i == n:
                return profit



            if buyFlag:
                profit1 = dfs(prices, i+1, n, profit - prices[i], False,True)
                profit2 = dfs(prices, i+1, n, profit, True, False)
            elif sellFlag:
                profit1 = dfs(prices, i+1, n, profit + prices[i], False, False)
                profit2 = dfs(prices, i+1, n, profit, False, True)
            else:
                return dfs(prices, i+1, n, profit, True, False)

            if profit1 > profit2:
                return profit1
            else:
                return profit2
            
            


        maxProfit = dfs(prices, 0, len(prices), 0, True, False)
        return maxProfit


            

