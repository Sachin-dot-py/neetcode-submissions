class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removed = 0
        latest_end_time = float('-inf')
        for start, end in intervals:
            if start < latest_end_time:
                removed += 1
            else:
                latest_end_time = max(end, latest_end_time)
        return removed
            