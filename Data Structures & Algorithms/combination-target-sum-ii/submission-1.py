from collections import defaultdict
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        counts = defaultdict(int)
        for c in candidates:
            counts[c] += 1

        keys = list(counts.keys())
        keys.sort()
        n = len(keys)


        def recur(keys, counts, target, curSet):
            if target < 0 or len(keys) == 0 or counts[keys[0]] < 0:
                return

            if target == 0:
                answer.append(curSet)
                return


            




            counts1 = counts.copy()
            counts2 = counts.copy()
            keys1 = keys.copy()
            keys2 = keys.copy()
            
            set1 = curSet.copy()
            set2 = curSet.copy()

            # Case 1
            counts1[keys[0]] -= 1
            set1.append(keys[0])
            recur(keys, counts1, target - keys[0], set1)

            # Case 2
            recur(keys[1:], counts2, target, set2)

        recur(keys, counts, target, [])



        return answer