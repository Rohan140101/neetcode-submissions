from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sorting
        hashmap = defaultdict(list)
        for s in strs:
            hashmap[''.join(sorted(s))].append(s)

        return list(hashmap.values())
        