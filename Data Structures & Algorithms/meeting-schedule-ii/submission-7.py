"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        heap = []
        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
        return len(heap)
        # if not intervals:
        #     return 0
        
        # intervals.sort(key=lambda x: x.end)
        # merged = []
        
        # for interval in intervals:
        #     if merged and merged[-1][1] > interval.start:
        #         merged[-1][2] += 1
        #         merged[-1][1] = max(merged[-1][1], interval.end)
        #     else:
        #         merged.append([interval.start, interval.end, 1])
        # return max([interval[2] for interval in merged])