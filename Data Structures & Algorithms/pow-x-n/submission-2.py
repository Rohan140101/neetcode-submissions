class Solution:
    def myPow(self, x: float, n: int) -> float:


        def posMyPow(x, n):
            if(n==1):
                return x

            if (n == 0):
                return 1

            l = n//2
            r = n - l
            # print(n, l, r)
            return posMyPow(x, l) * posMyPow(x, r)


        ans = posMyPow(x, abs(n))
        if n < 0:
            return 1/ans
        return ans