from queue import PriorityQueue
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums[:k]:
            heapq.heappush(self.heap, num)
        for num in nums[k:]:
            if num > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        if val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]
        
