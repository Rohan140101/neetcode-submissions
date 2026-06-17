class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterTracker = dict()
        for i in range(len(s)):
            if s[i] not in letterTracker:
                letterTracker[s[i]] = [i,i]
            else:
                letterTracker[s[i]][1] = i

        letterTracker = {k: v for (k, v) in sorted(letterTracker.items(), key=lambda x: x[1][0])}
        answer = []
        pStart = 0
        pEnd = 0
        for lStart, lEnd in letterTracker.values():
            # print(lStart, lEnd, pStart, pEnd)
            if lStart > pEnd:
                answer.append(pEnd - pStart + 1)
                pStart = lStart
                pEnd = lEnd
            else:
                pEnd = max(pEnd, lEnd)
        answer.append(pEnd - pStart + 1)
        return answer

        