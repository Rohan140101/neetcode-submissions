class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixMulti = [None for i in range(n)]
        suffixMulti = [None for i in range(n)]
        prefixMulti[0] = nums[0]
        suffixMulti[n-1] = nums[-1]

        for i in range(1, n):
            prefixMulti[i] = prefixMulti[i-1]*nums[i]
            suffixMulti[n-i-1] = suffixMulti[n-i] * nums[n-i-1]

        answer = [None for i in range(n)]
        for i in range(n):
            if i > 0:
                l = prefixMulti[i-1]
            else:
                l = 1

            if i < n - 1:
                r = suffixMulti[i+1]
            else:
                r = 1

            answer[i] = l * r
        return answer

        