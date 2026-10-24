class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # earliest end time

        result = []
        for start, end in intervals:
            if not result or result[-1][1] < start:
                result.append([start, end])
            else:
                result[-1] = [
                    min(result[-1][0], start),
                    max(result[-1][1], end)
                ]
        return result
