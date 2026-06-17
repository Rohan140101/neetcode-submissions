from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        landVal = 2**31 - 1
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j,0))
        vis = [[0 for i in range(n)] for j in range(m)]
        while queue:
            # print(queue)
            i, j, val = queue.popleft()
            if vis[i][j]:
                continue
            vis[i][j] = 1
            # if val == waterVal:
            #     continue
            # if grid[i][j] >= 1:
            #     continue
            grid[i][j] = val
            # elif val < grid[i][j]:
            #     grid[i][j] = val

            for k, l in neighbors:
                x = i + k
                y = j + l
                if x < 0 or x == m or y < 0 or y == n:
                    continue
                if grid[x][y] == landVal:
                    queue.append((x, y, val+1))
                
         

            


            


            
        