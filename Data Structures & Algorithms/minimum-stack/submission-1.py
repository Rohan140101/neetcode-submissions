class MinStack:

    def __init__(self):
        self.min_value = None
        self.stack = []
        self.min_stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min_stack:
            self.min_stack.append(min(value, self.min_stack[-1]))
        else:
            self.min_stack.append(value)

            
    def pop(self) -> None:
        val = self.stack.pop()
        self.min_stack.pop()
        return val

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()