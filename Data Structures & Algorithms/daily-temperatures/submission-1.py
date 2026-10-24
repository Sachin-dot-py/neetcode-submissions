class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute Force
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temp:
                    result[i] = j - i
                    break
        return result