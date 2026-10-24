class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(current_sum, chosen_nums, i):
            if current_sum > target:
                return
            if current_sum == target:
                res.append(chosen_nums[:])
                return
            for j in range(i, len(nums)):
                chosen_nums.append(nums[j])
                backtrack(current_sum + nums[j], chosen_nums, j)
                chosen_nums.pop()

        res = []
        chosen_nums = []
        backtrack(0, chosen_nums, 0)
        return res