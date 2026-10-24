class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(i, selected, current):
            if current > target or i >= len(nums):
                return
            elif current == target:
                results.append(selected)
                return
            dfs(i, selected + [nums[i]], current + nums[i])
            dfs(i + 1, selected, current)

        dfs(0, [], 0)
        return results