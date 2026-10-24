from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}": "{", "]": "[", ")": "("}
        stack = deque()
        for char in s:
            if char in closeToOpen:
                if not (stack and stack.pop() == closeToOpen[char]):
                    return False
            else:
                stack.append(char)
        return len(stack) == 0