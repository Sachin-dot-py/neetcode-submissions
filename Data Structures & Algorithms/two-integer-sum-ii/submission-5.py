import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            search = target - numbers[i]
            bis = bisect.bisect_left(numbers, search, i + 1)
            if bis < len(numbers) and numbers[bis] == search:
                return [i + 1, bis + 1]