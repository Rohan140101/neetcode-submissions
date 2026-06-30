class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hashset = set()
        n = len(nums)

        def dfs(num, perm, nums):
            # if len(perm) == n:
            #     hashset.add(tuple(perm))
            #     return

            newPerm = perm.copy()
            if num != None:
                newPerm.append(num)
            
            if len(newPerm) == n:
                hashset.add(tuple(newPerm))
                return


            for j in range(len(nums)):
                dfs(nums[j], newPerm, nums[:j] + nums[j+1:])

        dfs(None, list(), nums)    
        hashset = [list(x) for x in hashset]
        return hashset              


