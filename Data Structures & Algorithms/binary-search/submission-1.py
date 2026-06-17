class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        

        def binary_search(nums, target, start, end):
            if start > end:
                return -1



            mid = (start + end) // 2 
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return binary_search(nums, target, mid+1, end)
            else: 
                return binary_search(nums, target, start, mid-1)


            
        return binary_search(nums, target, 0, n-1)
        