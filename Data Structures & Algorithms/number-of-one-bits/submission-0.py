class Solution:
    def hammingWeight(self, n: int) -> int:
        setBits = 0
        while n:
            setBits += n%2
            n = n//2

        return setBits
        