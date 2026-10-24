from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First, count frequencies
        frequencies = defaultdict(int) # num: frequency O(n)
        for num in nums: # O(n) where n is len(nums)
            frequencies[num] += 1
        
        # Now get the top k frequent elements
        heap = [] # O(k) in O(n)
        for num, frequency in frequencies.items(): # O(nlogk)
            heapq.heappush(heap, (frequency, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]