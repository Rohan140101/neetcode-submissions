from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodeTime = [None for i in range(n)]

        adj_list = defaultdict(list)
        for start, end, t in times:
            adj_list[start].append((end, t))
        
        minheap = [(0, k)]
        while minheap:

            cur_time, node = heapq.heappop(minheap)
            if nodeTime[node - 1] != None:
                continue


            nodeTime[node - 1] = cur_time

            for neighbor, t in adj_list[node]:
                heapq.heappush(minheap, (cur_time + t, neighbor))


        if None in nodeTime:
            return -1
        
        return max(nodeTime)