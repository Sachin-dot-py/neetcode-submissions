import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            search = target - numbers[i]
            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == search:
                    return [i + 1, mid + 1]
                elif numbers[mid] < search:
                    l = mid + 1
                else:
                    r = mid - 1
        