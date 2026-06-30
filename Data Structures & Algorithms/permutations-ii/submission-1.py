from collections import defaultdict
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # hashset = set()
        answer = []
        counts = defaultdict(int)
        n = len(nums)

        for i in range(n):
            counts[nums[i]] += 1

        def dfs(num, perm, counts):
            # if len(perm) == n:
            #     hashset.add(tuple(perm))
            #     return

            newPerm = perm.copy()
            if num != None:
                newPerm.append(num)
            
            if len(newPerm) == n:
                answer.append(newPerm)
                return

            newCounts = counts.copy()
            newCounts[num] -= 1
            for number, count in newCounts.items():
                if count > 0:
                    dfs(number, newPerm, newCounts)

        dfs(None, list(), counts)    
        # hashset = [list(x) for x in hashset]
        # return hashset              
# 

        return answer
