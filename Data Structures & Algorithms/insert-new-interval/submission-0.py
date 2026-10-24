class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        newStart, newEnd = newInterval
        added = False
        for start, end in intervals:
            if not added and start >= newStart:
                if result and result[-1][1] >= newStart:
                    result[-1][1] = max(newEnd, result[-1][1])
                else:
                    result.append([newStart, newEnd])
                added = True
            if result and result[-1][1] >= start:
                result[-1][1] = max(end, result[-1][1])
            else:
                result.append([start, end])
        if not added:
            if result and result[-1][1] >= newStart:
                result[-1][1] = max(newEnd, result[-1][1])
            else:
                result.append([newStart, newEnd])
        return result
