class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check Rows
        n = 9
        for i in range(n):
            hashset = set()
            for j in range(n):
                if board[i][j] == '.':
                    continue
                if board[i][j] in hashset:
                    return False
                hashset.add(board[i][j])
        # Check Columns
        for j in range(n):
            hashset = set()
            for i in range(n):
                if board[i][j] == '.':
                    continue
                if board[i][j] in hashset:
                    return False
                hashset.add(board[i][j])

        # Check Squares
        boundaries = [0, 3, 6, 9]
        for a in range(3):
            r1 = boundaries[a]
            r2 = boundaries[a+1]
            for b in range(3):
                c1 = boundaries[b]
                c2 = boundaries[b+1]
                hashset = set()
                for i in range(r1, r2):
                    for j in range(c1, c2):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in hashset:
                            return False
                        hashset.add(board[i][j])
        return True
        