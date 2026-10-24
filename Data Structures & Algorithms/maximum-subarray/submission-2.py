class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        largest_sum = nums[0]
        for num in nums[1:]:
            if current_sum >= 0:
                # Positive current sum means our sum will increase
                current_sum += num
            else:
                # Start subarray again from here
                # Negative current sum will decrease the sum
                current_sum = num
            largest_sum = max(largest_sum, current_sum)
        return largest_sum