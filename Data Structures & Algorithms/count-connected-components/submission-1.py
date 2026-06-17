from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        vis = [False for i in range(n)]
        components = 0

        def dfs(node, parent):
            if vis[node]:
                return
                
            vis[node] = True
            neighbors = adj_list[node]
            for neighbor in neighbors:
                if neighbor != parent:
                    dfs(neighbor, node)



        for i in range(n):
            if vis[i]:
                continue

            components += 1
            dfs(i, -1)


        return components        