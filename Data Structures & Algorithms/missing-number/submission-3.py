class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        value = 0
        for num in nums:
            value ^= num
        for n in range(len(nums) + 1):
            value ^= n
        return value