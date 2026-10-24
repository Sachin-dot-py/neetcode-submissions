from math import log2
class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        current = 1
        for i in range(1, n + 1):
            # Check if `i` is a power of 2
            if i & (i - 1) == 0:
                current = i
            output[i] = 1 + output[i - current]
        return output