class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        allSubsets = []
        def getSubset(nums, i, curSet, n):
            if i == n:
                allSubsets.append(curSet)
                return

            takeSet = curSet.copy()
            takeSet.append(nums[i])
            getSubset(nums, i+1, takeSet, n)
            getSubset(nums, i+1, curSet, n)

        getSubset(nums, 0, [], len(nums))
        return list(allSubsets)
        