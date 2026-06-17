class Solution:
    def dfs(self, grid, vis, i, j, n, m):
        if vis[i][j]:
            return
        vis[i][j] = 1
        neighbours = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
        for neighbour in neighbours:
            new_i = neighbour[0]
            new_j = neighbour[1]
            
            if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
                continue

            print(new_i, new_j, grid[new_i][new_j], vis[i][j])
            if grid[new_i][new_j] == "1" and vis[new_i][new_j] == 0:
                print('here1')
                self.dfs(grid, vis, new_i, new_j, n, m)
            
        return 
             


    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        islands = 0
        vis = [[0 for j in range(m)] for i in range(n)]
        # print(vis)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and vis[i][j] == 0:
                    self.dfs(grid, vis, i, j, n, m)
                    islands += 1


        return islands