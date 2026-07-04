class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        n = len(gas)
        for i in range(n):
            diff.append(gas[i] - cost[i])

        if sum(diff) < 0:
            return -1
        l = 0
        r = 0
        cur_diff = 0

        while r<n:
            cur_diff += diff[r]
            if cur_diff < 0:
                cur_diff = 0
                l = r+1
                r = l
            else:
                r = r+1
            

        return l 







        
        