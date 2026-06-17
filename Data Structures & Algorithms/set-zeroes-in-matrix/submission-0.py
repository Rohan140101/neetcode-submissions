class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # for i in range(m):
        #     for j in range(n):
        #         if i in rows or j in cols:
        #             matrix[i][j] = 0

        # Only Iterate relevant rows and cols
        for r in rows:
            for j in range(n):
                matrix[r][j] = 0

        for c in cols:
            for i in range(m):
                matrix[i][c] = 0



        # dfs solution


        