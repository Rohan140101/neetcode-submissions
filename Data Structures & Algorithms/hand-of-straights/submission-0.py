from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n%groupSize:
            return False


        hashmap = defaultdict(int)
        for num in hand:
            hashmap[num] += 1


        while hashmap:
            cur_num = min(hashmap.keys())
            for i in range(groupSize):
                if hashmap[cur_num]:
                    hashmap[cur_num] -= 1
                    if not hashmap[cur_num]:
                        hashmap.pop(cur_num)
                    cur_num += 1
                else:
                    return False

        return True
                    
                        



