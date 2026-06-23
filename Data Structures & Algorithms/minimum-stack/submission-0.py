class MinStack:

    def __init__(self):
        self.min_value = None
        self.stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min_value is None or value < self.min_value:
            self.min_value = value

    def pop(self) -> None:
        val = self.stack.pop()
        if self.stack:
            self.min_value = min(self.stack)
        else:
            self.min_value = None

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_value
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()