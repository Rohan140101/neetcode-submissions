class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref = 1
        suf = 1 

        maxProd = float('-inf')
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                maxProd = max(maxProd, 0)
                pref = 1
            else:
                pref = pref * nums[i]
                maxProd = max(maxProd, pref)

            if nums[n-1-i] == 0:
                maxProd = max(maxProd, 0)
                suf = 1
            else:
                suf = suf * nums[n-1-i]
                maxProd = max(maxProd, suf)

            # maxProd = max(maxProd, pref, suf)

        return maxProd

            

            
        