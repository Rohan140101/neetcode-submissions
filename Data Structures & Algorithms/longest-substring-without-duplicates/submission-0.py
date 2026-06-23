from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        longestSubLen = 0


        l = 0
        r = 0
        n = len(s)

        while r < n:
            if s[r] in hashmap:
                longestSubLen = max(longestSubLen, r - l)
                idx = hashmap[s[r]]
                while l <= idx:
                    hashmap.pop(s[l])
                    l += 1

            hashmap[s[r]] = r
            r += 1
        longestSubLen = max(longestSubLen, r - l)
        return longestSubLen