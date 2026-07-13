class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # O(m*n)
        # m = len(matrix)
        # n = len(matrix[0])

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == target:
        #             return True

        # return False

        # O(m+n)
        # m = len(matrix)
        # n = len(matrix[0])

        # for i in range(m):
        #     if target >= matrix[i][0] and target <= matrix[i][n-1]:
        #         for j in range(n):
        #             if target == matrix[i][j]:
        #                 return True
        #         return False
                

        # Binary Search

        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m * n - 1

        while low <= high:
            mid = (low + high) // 2
            mid_r = mid // n
            mid_c = mid % n
            if matrix[mid_r][mid_c] == target:
                return True
            elif matrix[mid_r][mid_c] < target:
                low = mid + 1
            else:
                high = mid - 1
         
        return False