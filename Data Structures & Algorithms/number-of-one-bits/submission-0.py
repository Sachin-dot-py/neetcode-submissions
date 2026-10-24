class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        for i in range(32, -1, -1):
            if n // 2**i >= 1:
                n -= 2**i
                num += 1
        return num