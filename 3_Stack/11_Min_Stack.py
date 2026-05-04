class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(val if not self.minStack else min(val, self.minStack[-1]))
    
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]



class MinStack():
    
    def __init__(self):
        self.stack = []
        self.minVal = float("infinity")

    def push(self, val):
        if not self.stack:
            self.stack.append(0)
            self.minVal = val
        else:
            self.stack.append(val - self.minVal)
            if self.minVal > val:
                self.minVal = val
    def top(self):
        top_val = self.stack[-1]
        if top_val > 0:
            return top_val + self.minVal
        else:
            return self.minVal
    def pop(self):
        popped_val = self.stack.pop()
        if popped_val < 0:
            self.minVal = self.minVal - popped_val
    def getMin(self):
        return self.minVal