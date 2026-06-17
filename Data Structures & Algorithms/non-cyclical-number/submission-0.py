class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set()

        while True:
            if n in vis:
                return False
            vis.add(n)  
            ssd = 0
            while n:
                unit = n%10
                n = n // 10
                ssd += unit ** 2
            if ssd == 1:
                return True
            n = ssd

        