class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in paren_map:
                if not stack or stack.pop() != paren_map[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0