class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = [(x, y) for x, y in zip(position, speed)]
        
        zipped = sorted(zipped, key=lambda x: x[0], reverse=True)
        stack = []
        for ele in zipped:
            if not stack:
                stack.append(ele)
            
            top = stack[-1]
            top_time = (target - top[0])/top[1]
            ele_time = (target - ele[0])/ele[1]

            if ele_time > top_time:
                stack.append(ele)

        return len(stack)

       