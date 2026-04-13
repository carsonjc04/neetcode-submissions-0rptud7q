class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals = [[1,5],[2,4],[6,7]]
        # output = [[1,5], [6,7]]
        # 1. Sort intervals
        # 2. for start, end in intervals: if lastEnd <= start: output[-1][1] = max(end, lastEnd) else: output.append([start,end])

        intervals.sort(key = lambda i : i[0])

        output = [intervals[0]]
        for start, end in intervals:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd)
            else:
                output.append([start, end])
        return output



        

