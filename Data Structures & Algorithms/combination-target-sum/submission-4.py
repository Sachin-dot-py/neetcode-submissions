class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(current_sum, chosen_nums, i):
            if current_sum > target or i >= len(nums):
                return
            if current_sum == target:
                res.append(chosen_nums[:])
                return
            chosen_nums.append(nums[i])
            backtrack(current_sum + nums[i], chosen_nums, i)
            chosen_nums.pop()
            backtrack(current_sum, chosen_nums, i + 1)

        res = []
        backtrack(0, [], 0)
        return res