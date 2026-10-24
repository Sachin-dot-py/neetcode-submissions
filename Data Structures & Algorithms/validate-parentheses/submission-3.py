from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "}": "{", "]": "["}
        stack = deque()
        for c in s:
            if c in brackets:
                if not (stack and stack.pop() == brackets[c]):
                    return False
            else:
                stack.append(c)
        return len(stack) == 0