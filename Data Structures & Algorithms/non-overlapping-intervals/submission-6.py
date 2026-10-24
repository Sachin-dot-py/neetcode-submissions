class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) # earliest end time
        new_intervals = []
        for start, end in intervals:
            if not new_intervals or new_intervals[-1][1] <= start:
                new_intervals.append([start, end])
        return len(intervals) - len(new_intervals)