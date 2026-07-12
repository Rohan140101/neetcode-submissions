from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # Sorting
        # hashmap = defaultdict(list)
        # for s in strs:
        #     hashmap[''.join(sorted(s))].append(s)

        # return list(hashmap.values())
        

        # Tuple
        hashmap = defaultdict(list)
        for s in strs:
            counts = [0 for i in range(26)]
            for c in s:
                counts[ord(c) - ord('a')] += 1
            hashmap[tuple(counts)].append(s)

        return list(hashmap.values())
