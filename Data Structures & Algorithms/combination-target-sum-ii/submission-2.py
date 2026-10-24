class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(current_sum, idx, chosen):
            if current_sum == target:
                res.append(chosen[:])
                return
            if current_sum > target or idx >= len(candidates):
                # out of bounds - prune
                return

            # include
            chosen.append(candidates[idx])
            backtrack(current_sum + candidates[idx], idx + 1, chosen)
            chosen.pop()
            # exclude
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backtrack(current_sum, idx + 1, chosen)
            

        candidates.sort()
        res = []
        backtrack(0, 0, [])
        return res