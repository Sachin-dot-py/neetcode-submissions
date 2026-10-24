class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        for bit in range(32):
            bit_a = (a & (1 << bit))
            bit_b = (b & (1 << bit))
            if bit_a & bit_b:
                if carry:
                    res |= (1 << bit)
                carry = 1
            elif bit_a ^ bit_b:
                if carry:
                    carry = 1
                else:
                    res |= (1 << bit)
            else:
                if carry:
                    carry = 0
                    res |= (1 << bit)

        if res > 0x7FFFFFFF:
            res = ~(res ^ 0xFFFFFFFF)
        return res
            