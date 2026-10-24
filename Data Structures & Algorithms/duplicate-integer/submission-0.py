class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if n == m and i != j:
                    return True
        return False