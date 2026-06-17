class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack  = []
        ans = None

        operators = ["+", "-", "*",  "/"]
        for char in tokens:
            if char in operators:
                y = stack.pop()
                x = stack.pop()
                if char == "+":
                    ans = int(x + y)
                if char == "-":
                    ans = int(x - y)
                if char == "*":
                    ans = int(x * y)
                if char == "/":
                    ans = int(x / y)

                stack.append(ans)
            else:
                stack.append(int(char))
            # print(stack)

        return stack.pop()
                    
        
        