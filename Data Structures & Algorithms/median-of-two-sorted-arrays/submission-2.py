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


        # # 2 Pointer
        # n1 = len(nums1)
        # n2 = len(nums2)
        # total = n1 + n2
        # half = total // 2 + 1
        # m1, m2 = None, None
        # i, j = 0, 0
        # for _ in range(half):
        #     m2 = m1
        #     if i < n1 and j < n2:
        #         if nums1[i] < nums2[j]:
        #             m1 = nums1[i]
        #             i += 1
        #         else:
        #             m1 = nums2[j]
        #             j += 1
        #     elif i < n1:
        #         m1 = nums1[i]
        #         i += 1
        #     else:
        #         m1 = nums2[j]
        #         j += 1


        # if total % 2:
        #     return m1
        # else:
        #     return (m1 + m2) / 2

        # Binary Search

        def getMedian(a, b):
            n1 = len(a)
            n2 = len(b)
            if n2 < n1:
                return getMedian(b, a)

            half = (n1 + n2) // 2


            low1, high1 = 0, n1
            low2, high2 = 0, n2
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')

            while True:
                
                mid1 = (low1 + high1) // 2
                mid2 = half - mid1
                print("low1:", low1, ", mid1:", mid1, ", high1:", high1)
                print("low2:", low2, ", mid2:", mid2, ", high2:", high2)

                if mid1 == 0:
                    l1 = float('-inf')
                else:
                    l1 = a[mid1 - 1]

                if mid1 == n1:
                    r1 = float('inf')
                else:
                    r1 = a[mid1]

                if mid2 == 0:
                    l2 = float('-inf')
                else:
                    l2 = b[mid2 - 1]

                if mid2 == n2:
                    r2 = float('inf')
                else:
                    r2 = b[mid2]

                    
                if r1 >= l2 and r2 >= l1:
                    break


                if l2 > r1:
                    low1 = mid1 + 1
                elif l1 > r2:
                    high1 = mid1 - 1



            if (n1 + n2) % 2:
                return min(r1, r2)
            else:
                return (max(l1, l2) + min(r1, r2)) / 2

        return getMedian(nums1, nums2)
                

                

            



        

        
        