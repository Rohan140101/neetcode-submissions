class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [['.' for j in range(n)] for i in range(n)]

        answer = []

        def isSafe(board, r, c):
            r1 = r
            c1 = c
            # Look Left
            while c1 >= 0:
                if board[r1][c1] == 'Q':
                    return False
                c1 -= 1


            # Look Left Top
            r1 = r
            c1 = c
            while r1 >= 0 and c1 >= 0:
                if board[r1][c1] == 'Q':
                    return False

                r1 -= 1
                c1 -= 1

            # Look Left Bottom
            r1 = r
            c1 = c
            while r1 < n and c1 >= 0:
                if board[r1][c1] == 'Q':
                    return False

                r1 += 1
                c1 -= 1

            return True

        def recur(c, board):
            # print(c, board)
            if c == n:
                # print(board)
                # print()
                newBoard = [row.copy() for row in board]
                answer.append(newBoard)
                return


            for r in range(n):
                if isSafe(board, r, c):
                    board[r][c] = 'Q'
                    recur(c+1, board)
                    board[r][c] = '.'

        recur(0, board)
        for i in range(len(answer)):
            for j in range(len(answer[i])):

                answer[i][j] = "".join(answer[i][j])

        return answer

                