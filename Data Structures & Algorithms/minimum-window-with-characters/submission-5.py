from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # n = len(s)
        # hashmap = defaultdict(int)

        # for char in t:
        #     hashmap[char] += 1

        # minLen = float('inf')
        # minStr = ""
        # for i in range(n):
        #     for j in range(i, n):
        #         newMap = hashmap.copy()
        #         # print(i, j, newMap, )
        #         for k in range(i, j+1):
        #             if s[k] in newMap:
        #                 newMap[s[k]] -= 1
        #                 if newMap[s[k]] == 0:
        #                     newMap.pop(s[k])

        #             if not newMap:
        #                 # print('here1/')
        #                 if minLen > j - i + 1:
        #                     minLen = j - i + 1
        #                     minStr = s[i:j+1]
        #                 break


        # return minStr

        n = len(s)
        hashmap = defaultdict(int)
        for i in range(len(t)):
            hashmap[t[i]] += 1

        need = len(hashmap.keys())
        have = 0

        l = 0
        r = 0

        # minLen = float('inf')
        minStr = None
        needMap = defaultdict(int)
        while r < n:
            if s[r] in hashmap:
                needMap[s[r]] += 1

                if needMap[s[r]] == hashmap[s[r]]:
                    have += 1
            while have == need and l <= r:
                if not minStr or len(minStr) > r+1-l:
                    minStr = s[l:r+1]

                if s[l] in needMap:
                    needMap[s[l]] -= 1
                    
                    if needMap[s[l]] < hashmap[s[l]]:
                        have -= 1
                    
                l += 1

            r += 1



        if minStr:
            return minStr


        return ""


        