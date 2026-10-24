class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(openN, closedN):
            if openN == closedN == n:
                strings.append("".join(stack))
                return
            elif openN > n or closedN > n:
                return
            else:
                if openN > closedN:
                    stack.append(")")
                    dfs(openN, closedN + 1)
                    stack.pop()
                stack.append("(")
                dfs(openN + 1, closedN)
                stack.pop()

        stack = []
        strings = []
        dfs(0, 0)
        return strings
