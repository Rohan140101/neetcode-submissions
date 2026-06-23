from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""


        originalMap = defaultdict(int)
        n = len(s)
        m = len(t)

        for i in range(m):
            originalMap[t[i]] += 1

        minWindowSubstring = None
        l = 0
        r = 0
        need = len(originalMap.keys())
        have = 0
        windowMap = defaultdict(int)
        # print(originalMap)
        while r < n:
            if s[r] in originalMap.keys():
                windowMap[s[r]] += 1
                if windowMap[s[r]] == originalMap[s[r]]:
                    have += 1
            # print(l, r, need, have, windowMap, minWindowSubstring)
            while need == have and l <= r:
                # print(l, r)
                if minWindowSubstring == None or len(minWindowSubstring) > r - l + 1:
                    minWindowSubstring = s[l:r+1]
                if s[l] in originalMap.keys():
                    windowMap[s[l]] -= 1
                    # if windowMap[s[l]] == 0:
                    if windowMap[s[l]] < originalMap[s[l]]:
                        have -= 1
                    # have -= 1
                    # l += 1
                    # break
                    

                l += 1

            r += 1

        if minWindowSubstring == None:
            return ""
        return minWindowSubstring

                