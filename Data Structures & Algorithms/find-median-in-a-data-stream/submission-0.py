"""
If we used a sorted list:
addNum would be O(n)
findMedian would be O(1)
Just store the list, space O(n)

If we used an unsorted list:
addNum would be O(1)
findMedian would be O(nlogn), space O(n)

If we used two heaps each of size n/2
addNum would be O(logn)
findMedian would be O(1)
Store largerHalf, smallerHalf both heaps
largerHalf - min heap
smallerHalf - max heap
the first n/2 should be in smallerHalf

median if odd: (n // 2 - 1)th element
median if even: average of (n // 2 - 1) and (n // 2)th index element

smallerHalf size should be n // 2 (would have till index n // 2 - 1)
so heappush elements to smallHalf, heappop, then heappush to largerHalf
"""

import heapq

class MedianFinder:

    def __init__(self):
        self.small = [] # max-heap
        self.large = [] # min-heap

    def addNum(self, num: int) -> None:
        # Always push to small first, then large, then rebalance
        heapq.heappush(self.small, -num)

        largest_in_small = -heapq.heappop(self.small)
        heapq.heappush(self.large, largest_in_small)

        if len(self.large) > len(self.small):
            smallest_in_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest_in_large)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            # odd
            return -self.small[0]
        else:
            # even
            return (-self.small[0] + self.large[0]) / 2.0
        
        