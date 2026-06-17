class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = dict()
        for char in s:
            if char not in hashmap:
                hashmap[char] = 0
            hashmap[char] += 1

        for char in t:
            if char not in hashmap:
                return False
            hashmap[char] -= 1
            if not hashmap[char]:
                hashmap.pop(char)

        if hashmap:
            return False

        return True


        