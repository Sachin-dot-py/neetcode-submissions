class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, current):
            if idx == len(nums):
                res.append(current[:])
            if idx >= len(nums):
                return
            # include
            current.append(nums[idx])
            backtrack(idx + 1, current)
            current.pop()
            # exclude
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                # skip same element
                idx += 1
            backtrack(idx + 1, current)

        nums.sort()
        res = []
        backtrack(0, [])
        return res