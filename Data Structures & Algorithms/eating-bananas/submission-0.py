from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            hours = 0
            for num in piles:
                hours += ceil(num / k)
            return hours <= h
        
        low, high = 1, max(piles)
        lowest_k = -1
        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                lowest_k = mid
                high = mid - 1
            else:
                low = mid + 1
        return lowest_k
