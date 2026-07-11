# from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


        # Hashmap
        hashmap = dict()
        for i in range(len(nums)):

            toFind = target - nums[i]
            if toFind in hashmap.keys():
                return [hashmap[toFind], i]
            hashmap[nums[i]] = i




        
        