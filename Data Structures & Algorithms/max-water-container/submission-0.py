class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = float('-inf')
        n = len(height)
        i = 0 
        j = n-1

        while i < j:
            minVal = min(height[i], height[j])
            area = max(area, minVal * (j-i))
            if height[i] < height[j]:
                while i < j and height[i+1] < height[i]:
                    i += 1
                i += 1
            elif height[i] > height[j]:
                while i < j and height[j-1] < height[j]:
                    j -= 1
                j -= 1
            else:
                if height[i+1] > height[j-1]:
                    i += 1
                else:
                    j -= 1

        return area

        