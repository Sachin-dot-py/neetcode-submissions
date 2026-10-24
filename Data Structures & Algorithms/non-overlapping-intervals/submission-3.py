class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        intervals.sort(key=lambda x: x[1])
        to_remove = 0
        for start, end in intervals:
            if res and start < res[-1][1]:
                to_remove += 1
            else:
                res.append([start, end])
        return to_remove