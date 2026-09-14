class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort()

        if end_i >= next_start_i:
            res.append([start_i, max(end_i,next_end_i])
        
        [1,4], [2,3]
        """

        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if res[-1][1] >= start:
                res[-1] = [res[-1][0], max(end, res[-1][1])]
            else:
                res.append([start, end])
        return res

