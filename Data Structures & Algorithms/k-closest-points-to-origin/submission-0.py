import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distanceFromOrigin = dict()
        # n = len(points)
        # for i in range(n):
        #     point = points[i]
        #     distance = (point[0]**2 + point[1]**2)**0.5
        #     distanceFromOrigin[i] = distance

        # # print(sorted(distanceFromOrigin.items(), key=lambda x: x[1])[:k])
        # closestPoints = [points[i] for i, d in sorted(distanceFromOrigin.items(), key=lambda x: x[1])[:k]]
        # # print(closestPoints)
        # return closestPoints

        heap = []
        n = len(points)
        for i in range(n):
            point = points[i]
            distance = (point[0]**2 + point[1]**2)**0.5
            heapq.heappush(heap, (distance, i))

        closestPoints = []
        for i in range(k):
            distance, pointIdx = heapq.heappop(heap)
            closestPoints.append(points[pointIdx])

        return closestPoints

        

