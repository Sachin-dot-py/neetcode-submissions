from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile / k)
                if hours > h:
                    return False
            return True

        low, high = 1, max(piles)
        while low < high:
            mid = low + (high - low) // 2
            if possible(mid):
                high = mid
            else:
                low = mid + 1
        return low