class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        res = 0
        max_num = max(nums)
        for num in nums:
            res ^= num
        for num in range(max_num + 1):
            res ^= num
        return max_num + 1 if res == 0 else res