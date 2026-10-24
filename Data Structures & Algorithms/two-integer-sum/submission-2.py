class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for n, num in enumerate(nums):
            if target - num in seen:
                return [seen[target-num], n]
            seen[num] = n
            
