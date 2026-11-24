class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # split into two arrays with 0 as the pivot
        # both of these subarrays are sorted (negatives in descending order, poisitions in increasing)
        # merge!
        pivot = len(nums)
        for i, num in enumerate(nums):
            if num >= 0:
                pivot = i
                break
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        
        merged = []
        i = pivot
        j = pivot - 1
        while i < len(nums) and j >= 0:
            if nums[i] < nums[j]:
                merged.append(nums[i])
                i += 1
            else:
                merged.append(nums[j])
                j -= 1
        if i < len(nums):
            merged.extend(nums[i:])
        elif j >= 0:
            merged.extend(nums[j::-1])
        return merged