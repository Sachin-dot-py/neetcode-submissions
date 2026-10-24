from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First, count frequencies
        frequencies = defaultdict(int) # num: frequency
        for num in nums:
            frequencies[num] += 1
        
        heap = []
        for num, frequency in frequencies.items():
            heapq.heappush(heap, (frequency, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]