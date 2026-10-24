class Solution:
    def isValid(self, s: str) -> bool:
        conversion = {"(": ")", "{":"}", "[": "]"}
        stack = []
        for c in s:
            if c in conversion:
                stack.append(c)
            else:
                if not stack or conversion[stack.pop()] != c:
                    return False
        return len(stack) == 0
