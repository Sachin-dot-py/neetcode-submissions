import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        
        heap = []
        for num in freqs.keys():
            heapq.heappush(heap, (freqs[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [item[1] for item in heap]