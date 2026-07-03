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


        def recur(i, counts, target, curSet):
            if target < 0 or i == n or counts[keys[i]] < 0:
                return

            if target == 0:
                answer.append(curSet.copy())
                return

            # Case 1
            counts[keys[i]] -= 1
            curSet.append(keys[i])
            recur(i, counts, target - keys[i], curSet)

            # Case 2
            counts[keys[i]] += 1
            curSet.pop()
            recur(i + 1, counts, target, curSet)

        recur(0, counts, target, [])



        return answer