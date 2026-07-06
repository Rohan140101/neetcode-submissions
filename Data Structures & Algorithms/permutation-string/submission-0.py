from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)

        for i in range(len(s1)):
            hashmap1[s1[i]] += 1
            hashmap2[s2[i]] += 1

        def isCompleteMatch():
            for i in range(97, 123):
                if hashmap1[chr(i)] != hashmap2[chr(i)]:
                    return False

            return True


        
        for j in range(len(s1), len(s2)):
            if isCompleteMatch():
                return True
            i = j - len(s1)
            hashmap2[s2[i]] -= 1
            hashmap2[s2[j]] += 1

        if isCompleteMatch():
                return True
        return False 
        