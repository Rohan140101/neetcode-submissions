from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        hashmap = defaultdict(int)

        n = len(s)
        charRepLength = 0
        while r < n:
            hashmap[s[r]] += 1
            maxLetterCount = max(hashmap.values())
            # print(s[l:r+1], maxLetterCount, hashmap)
            if r + 1 - l - maxLetterCount <= k:
                # print("in if")
                charRepLength = max(charRepLength, r + 1 - l)
            else:
                # print("in else")
                while l < r and r + 1 - l - maxLetterCount > k:
                    hashmap[s[l]] -= 1
                    maxLetterCount = max(hashmap.values())
                    l += 1
                charRepLength = max(charRepLength, r + 1 - l)

            r += 1

        return charRepLength


        