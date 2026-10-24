class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for num in nums:
            if seen.get(num):
                return True
            seen[num] = True
        return False