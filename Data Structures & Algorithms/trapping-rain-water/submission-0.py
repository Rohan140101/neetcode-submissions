class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0 for i in range(n)]
        maxRight = [0 for i in range(n)]
        totalWater = 0

        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])

        for j in range(n-2, -1, -1):
            maxRight[j] = max(maxRight[j+1], height[j+1])

        for i in range(n):
            totalWater += max(0, min(maxLeft[i], maxRight[i]) - height[i])
        
        return totalWater
