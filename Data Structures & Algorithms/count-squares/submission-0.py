from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.allPointsCount = defaultdict(int)
        self.allPoints = set()
        

    def add(self, point: List[int]) -> None:
        self.allPointsCount[tuple(point)] += 1
        self.allPoints.add(tuple(point))

    def count(self, point: List[int]) -> int:
        res = 0
        for cur_point in self.allPoints:
            cur_x = cur_point[0]
            cur_y = cur_point[1]
            x = point[0]
            y = point[1]
            x_diff = abs(cur_x - x)
            y_diff = abs(cur_y - y)

            if x_diff != y_diff or x_diff == 0 or y_diff == 0:
                continue

            res += self.allPointsCount[cur_point] * self.allPointsCount[(x, cur_y)] * self.allPointsCount[(cur_x, y)] 
        return res
