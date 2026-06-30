class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []

        answer = [0 for i in range(n)]

        for i in range(n-1, -1, -1):
            val = None
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                answer[i] = stack[-1][1] - i
            else:
                answer[i] = 0

            stack.append((temperatures[i], i))

        return answer
            



        