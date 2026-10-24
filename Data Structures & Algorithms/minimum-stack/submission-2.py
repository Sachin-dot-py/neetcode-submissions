from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.prefixmin = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.prefixmin and self.prefixmin[-1] < val:
            self.prefixmin.append(self.prefixmin[-1])
        else:
            self.prefixmin.append(val)
        

    def pop(self) -> None:
        self.prefixmin.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefixmin[-1]
        
