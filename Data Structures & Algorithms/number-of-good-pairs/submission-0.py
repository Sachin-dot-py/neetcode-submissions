from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # 1 is repeated 3 times - 2 + 1 + 0 pairs from it
        # 3 is repeated 2 times - 1 + 0 pair from it
        # 2 is repeated 1 time - 0 pairs from it

        # 1 is repeated 4 times - 3 + 2 + 1 + 0 = 6 pairs from it

        # Count number of repetiions of each
        # For each number, add the pairs from it
        # Sum of numbers from 1 to n - 1 is n(n-1)/2

        count = Counter(nums)
        pairs = 0
        for value in count.values():
            pairs += (value * (value - 1)) // 2
        return pairs