class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        i = 0
        n = len(intervals)
        while i < n - 1:
            tmp1 = intervals[i]
            tmp2 = intervals[i + 1]
            if tmp1[-1] >= tmp2[0]:
                intervals[i] = [min(tmp1[0], tmp2[0]), max(tmp2[1], tmp1[1])]
                intervals.remove(intervals[i + 1])
                i -= 1
                n -= 1
            i += 1

        return intervals
