class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftStack = []
        rightStack = []
        
        
        n = len(heights)
        leftSme = [0 for i in range(n)]
        rightSme = [0 for i in range(n)]
        for i in range(n):
            while leftStack and leftStack[-1][0] >= heights[i]:
                leftStack.pop()

            if len(leftStack) == 0:
                leftSme[i] = 0
            else:
                val, idx = leftStack[-1]
                leftSme[i] = idx+1

            leftStack.append((heights[i], i))
                



        for j in range(n-1, -1, -1):
            while rightStack and rightStack[-1][0] >= heights[j]:
                rightStack.pop()

            if len(rightStack) == 0:
                rightSme[j] = n-1
            else:
                val, idx = rightStack[-1]
                rightSme[j] = idx-1
                # rightStack.append((heights[j], j))
            rightStack.append((heights[j], j))

        maxRectangle = 0
        print(leftSme, rightSme)
        for i in range(n):
            maxRectangle = max(maxRectangle, heights[i]*(rightSme[i] - leftSme[i] + 1))

        return maxRectangle
                


        