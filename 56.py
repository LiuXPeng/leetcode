# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        starts = []
        ends = []
        for L in intervals:
            starts.append(L.start)
            ends.append(L.end)
        starts.sort()
        ends.sort()
        i = 0
        res = []
        while i < len(starts) - 1:
            temp = [starts[i]]
            while i < len(starts) - 1 and ends[i] >= starts[i + 1]:
                i += 1
            res.append(temp + [ends[i]])
            i += 1
        if i < len(starts):
            res.append([starts[i], ends[i]])
        return res