class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        value = nums[0]
        for num in nums[1:]:
            value ^= num
        for n in range(len(nums) + 1):
            value ^= n
        return value