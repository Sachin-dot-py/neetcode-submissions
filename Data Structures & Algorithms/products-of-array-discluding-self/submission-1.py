class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        current = 1
        zero_count = 0
        for num in nums:
            if num:
                current *= num
            else:
                zero_count += 1
        if zero_count > 1:
            return output
        
        for i, c in enumerate(nums):
            if zero_count:
                output[i] = 0 if c else current
            else:
                output[i] = current // c
        return output
