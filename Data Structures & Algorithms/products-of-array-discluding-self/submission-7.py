class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeroes = 0
        for num in nums:
            if num == 0:
                num_zeroes += 1
        
        if num_zeroes >= 2:
            return [0] * len(nums)
        
        product = 1
        for num in nums:
            if num != 0:
                product *= num

        result = [0] * len(nums)
        for i, num in enumerate(nums):
            if num_zeroes == 0:
                result[i] = product // num
            else:
                if num == 0:
                    result[i] = product
                    break
        return result