class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        def recur(nums, curSet, target):
            if target == 0:
                ans.append(curSet)
                return

            if len(nums) == 0 or target < 0:
                return 

            set1 = curSet.copy()
            set2 = curSet.copy()
            set1.append(nums[0])
            recur(nums, set1, target - nums[0])
            # curSet.pop()
            recur(nums[1:], set2, target)

        recur(nums, [], target)
        return ans





            
