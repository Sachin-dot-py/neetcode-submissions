class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index = stack.pop()[0]
                result[index] = i - index
            stack.append((i, temp))
        return result