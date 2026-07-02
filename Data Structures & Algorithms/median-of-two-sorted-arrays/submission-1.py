class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # # Brute Force
        # for ele in nums2:
        #     nums1.append(ele)

        # nums1.sort()
        # n = len(nums1)
        # if n % 2:
        #     return nums1[n//2]
        # else:
        #     return (nums1[n//2 - 1] + nums1[n//2]) / 2


        # 2 Pointer
        n1 = len(nums1)
        n2 = len(nums2)
        total = n1 + n2
        half = total // 2 + 1
        m1, m2 = None, None
        i, j = 0, 0
        for _ in range(half):
            m2 = m1
            if i < n1 and j < n2:
                if nums1[i] < nums2[j]:
                    m1 = nums1[i]
                    i += 1
                else:
                    m1 = nums2[j]
                    j += 1
            elif i < n1:
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1


        if total % 2:
            return m1
        else:
            return (m1 + m2) / 2
            



        

        
        