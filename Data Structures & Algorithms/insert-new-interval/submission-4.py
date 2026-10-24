class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            if end < newInterval[0]:
                new_intervals.append([start, end])
            elif start > newInterval[1]:
                new_intervals.append(newInterval)
                return new_intervals + intervals[i:]
            else:
                newInterval = [
                    min(newInterval[0], start),
                    max(newInterval[1], end)
                ]
        new_intervals.append(newInterval)
        return new_intervals