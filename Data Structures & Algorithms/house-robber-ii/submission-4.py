class Solution:
    def rob(self, nums: List[int]) -> int:
        def houserobber1(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            
            n = len(nums)
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            
            return dp[n - 1]
        if len(nums) == 1:
            return nums[0]
        
        return max(houserobber1(nums[1:]), houserobber1(nums[:-1]))