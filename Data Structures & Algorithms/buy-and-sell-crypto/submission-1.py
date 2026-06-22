class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # n = len(prices)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         profit = max(profit, prices[j] - prices[i])

        # return profit
        # n = len(prices)
        # leftMinArr = [0 for i in range(n)]
        # rightMaxArr = [0 for i in range(n)]
        # leftMin = float('inf')
        # rightMax = float('-inf')
        # for i in range(n):
        #     cur = prices[i]
        #     if cur < leftMin:
        #         leftMin = cur
        #     leftMinArr[i] = leftMin


        # for i in range(n-1, -1, -1):
        #     cur = prices[i]
        #     if cur > rightMax:
        #         rightMax = cur
        #     rightMaxArr[i] = rightMax

        # profit = 0
        # for i in range(n):
        #     profit = max(profit, rightMaxArr[i] - leftMinArr[i])

        # return profit
        l, r = 0, 1

        n = len(prices)
        profit = 0
        while r < n:
            diff = prices[r] - prices[l]
            if diff > 0:
                profit = max(diff, profit)
                r += 1
            else:
                l = r
                r += 1

        return profit
            