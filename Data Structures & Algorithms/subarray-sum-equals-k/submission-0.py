from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append(nums[i] + prefixSum[i-1])

        hashmap = defaultdict(int)
        hashmap[0] = 1

        subArrays = 0
        for i in range(len(nums)):
            valToFind = prefixSum[i] - k
            subArrays += hashmap[valToFind]
            hashmap[prefixSum[i]] += 1
            

        return subArrays


        