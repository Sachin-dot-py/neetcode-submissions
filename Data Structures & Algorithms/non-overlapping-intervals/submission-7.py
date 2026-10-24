class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) # earliest end time
        new_intervals = 1
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if not new_intervals or prevEnd <= start:
                new_intervals += 1
                prevEnd = end
        return len(intervals) - new_intervals