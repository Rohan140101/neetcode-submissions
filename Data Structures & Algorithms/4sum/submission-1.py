from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # # Hashmap
        # nums.sort()
        # hashmap = defaultdict(int)
        # n = len(nums)
        # for i in range(n):
        #     hashmap[nums[i]] += 1


        # results = set()
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         for k in range(j+1, n):
        #             newMap = hashmap.copy()
        #             newMap[nums[i]] -= 1
        #             newMap[nums[j]] -= 1
        #             newMap[nums[k]] -= 1
        #             valToGet = target - nums[i] - nums[j] - nums[k]
        #             if newMap[valToGet] > 0:
        #                 ans = [nums[i], nums[j], nums[k], valToGet]
        #                 ans.sort()
        #                 results.add(tuple(ans))

        # results = [list(x) for x in results]

        # return results

        # Two Pointer

        n = len(nums)
        result = set()
        nums.sort()
        for i in range(n-3):
            for j in range(i+1, n-2):
                k = j + 1
                l = n - 1

                while k < l:
                    val = nums[i] + nums[j] + nums[k] + nums[l]
                    if val == target:
                        ans = (nums[i], nums[j], nums[k], nums[l])
                        result.add(ans)
                        k += 1
                        l -= 1
                    elif val > target:
                        l -= 1
                    else:
                        k += 1

        results = [list(x) for x in result]

        return results
        
                
        