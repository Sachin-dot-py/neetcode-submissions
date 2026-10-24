class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, current):
            res.add(tuple(current[:]))
            if idx >= len(nums):
                return
            # include
            current.append(nums[idx])
            backtrack(idx + 1, current)
            current.pop()
            # exclude
            backtrack(idx + 1, current)

        nums.sort()
        res = set()
        backtrack(0, [])
        return list(res)