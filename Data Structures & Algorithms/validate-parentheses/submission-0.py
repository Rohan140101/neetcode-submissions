class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '[', '{']
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for i in range(len(s)):
            if s[i] in open:
                stack.append(s[i])
            elif not stack or stack[-1] != mapping[s[i]]:
                return False
            else:
                stack.pop() 

        if stack:
            return False
        return True
                
        