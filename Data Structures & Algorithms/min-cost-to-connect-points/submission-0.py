from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = defaultdict(lambda : defaultdict(int))
        

        n = len(points)

        def get_manhattan_dist(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        for i in range(n):
            for j in range(n):
                if i != j:
                    adj_list[i][j] = get_manhattan_dist(points[i], points[j])


        
        min_heap = []
        dist = 0
        heapq.heappush(min_heap, (0, 0))
        vis = set()

        while len(vis) != n:
            distance, cur_node = heapq.heappop(min_heap)
            if cur_node not in vis:
                vis.add(cur_node)
                dist += distance
                for neighbor, distance_from_cur_node in adj_list[cur_node].items():
                    heapq.heappush(min_heap, (distance_from_cur_node, neighbor))
        
        return dist

        
        

        