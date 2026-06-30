from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodeTime = [None for i in range(n)]


        adj_list = defaultdict(list)
        for start, end, t in times:
            adj_list[start].append((end, t))
        def dfs(node, time, visited):
            if node in visited:
                return

            if nodeTime[node - 1] == None:
                nodeTime[node - 1] = time
            elif time >= nodeTime[node - 1]:
                return
            else:
                nodeTime[node - 1] = min(nodeTime[node - 1], time)\

            newVisited = visited.copy()
            newVisited.add(node)
            for neighbor, t in adj_list[node]:
                dfs(neighbor, time+t, newVisited)


        dfs(k, 0, set())
        if None in nodeTime:
            return -1
        
        return max(nodeTime)