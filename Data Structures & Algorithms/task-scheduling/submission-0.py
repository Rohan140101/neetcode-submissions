from collections import deque, defaultdict
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque([None for i in range(n)])
        counts = defaultdict(int)

        for task in tasks:
            counts[task] += 1

        countHeap = []
        for task, count in counts.items():
            heapq.heappush(countHeap, (count * -1, task))

        def isQueueEmpty(queue):
            for ele in queue:
                if ele != None:
                    return False

            return True

        recentPop = None
        scheduler = 0
        
        while (not isQueueEmpty(queue)) or countHeap or recentPop:
            scheduler += 1
            # recentPop = queue.popLeft()
            if recentPop:
                heapq.heappush(countHeap, recentPop)

            if countHeap:
                count, task = heapq.heappop(countHeap)
                
                newCount = count + 1
                if newCount < 0:
                    queue.append((newCount, task))
                else:
                    queue.append(None)
            else:
                queue.append(None)
            # else:

            if not isQueueEmpty(queue):
                recentPop = queue.popleft()
            else:
                recentPop = None
            # print(queue, countHeap, recentPop, isQueueEmpty(queue), scheduler)
            # print((not isQueueEmpty(queue)) or countHeap or recentPop)

        return scheduler

            



            

            





        