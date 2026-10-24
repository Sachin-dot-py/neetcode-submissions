class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(current, subset, index):
            if current == target:
                result.append([x for x in subset])
                return
            if current > target:
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                backtrack(current + candidates[i], subset, i + 1)
                subset.pop()
            
        result = []
        candidates.sort()
        backtrack(0, list(), 0)
        return result