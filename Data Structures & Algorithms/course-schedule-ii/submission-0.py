from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        stack = []

        adj_list = defaultdict(list)

        for node1, node2 in prerequisites:
            adj_list[node2].append(node1)

        vis = [False for i in range(numCourses)] 
        
        def dfs(node, cycle):
            # print(node, cycle)
            if node in cycle:
                return False


            if vis[node]:
                return True

            

            vis[node] = True
            newCycle = cycle.copy()
            newCycle.add(node)

            val = True
            for neighbor in adj_list[node]:
               val = val and dfs(neighbor, newCycle)

            stack.append(node)
             
            return val

        for i in range(numCourses):
            if dfs(i, set()) == False:
                return []
        # print(stack)
        return stack[::-1]

        