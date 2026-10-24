class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = max(nums) # O(n)
        nums_set = set(nums)
        for num in range(max_num + 1):
            if num not in nums_set:
                return num
        return max_num + 1