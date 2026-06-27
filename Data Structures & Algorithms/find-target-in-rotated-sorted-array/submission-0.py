class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        # Finding Pivot
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m


        pivot = l

        def binary_search(left, right):
            # print("here", left, right)
            if not (target >= nums[left] and target <= nums[right]):
                return None

            while left <= right:
                
                mid = (left + right) // 2
                # print(left, right, mid)
                if nums[mid] == target:
                    return mid

                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1


            return None

        val = binary_search(0, pivot-1)
        if val != None:
            return val

        val = binary_search(pivot, n-1)
        if val != None:
            return val

        return -1