class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newStr = ""
        for i in range(len(s)):
            if (ord(s[i]) >= 97 and ord(s[i]) <= 122) or (ord(s[i]) >= 48 and ord(s[i]) <= 57):
                newStr += s[i]

        n = len(newStr)
        i = 0
        j = n - 1
        while i <= j:
            if newStr[i] == newStr[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

        
        
        