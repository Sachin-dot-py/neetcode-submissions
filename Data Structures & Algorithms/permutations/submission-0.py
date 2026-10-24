class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(perm, included):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for num in nums:
                if num not in included:
                    included.add(num)
                    perm.append(num)
                    backtrack(perm, included)
                    perm.pop()
                    included.remove(num)

        res = []
        included = set()
        backtrack([], included)
        return res