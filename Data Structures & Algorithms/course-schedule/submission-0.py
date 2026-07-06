from collections import deque,defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque([])
        indegreeCount = [0 for i in range(numCourses)]
        adj_list = defaultdict(list)
        for i, o in prerequisites:
            adj_list[o].append(i)
            indegreeCount[i] += 1

        
        for i in range(numCourses):
            if indegreeCount[i] == 0:
                queue.append(i)

        while queue:
            cur_course = queue.popleft()
            for c in adj_list[cur_course]:
                indegreeCount[c] -= 1
                if indegreeCount[c] == 0:
                    queue.append(c)

        for i in range(numCourses):
            if indegreeCount[i] > 0:
                return False

        return True           


            
        