class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        n = len(nums)
        # dp = [0] * n # dp[i] is max money from robbing houses 1..i
        prev2 = nums[0]
        prev = max(nums[0], nums[1])
        for i in range(2, n):
            current = max(nums[i] + prev2, prev)
            prev2, prev = prev, current
        
        return current
        