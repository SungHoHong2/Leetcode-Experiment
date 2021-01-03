class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals based the starting point
        intervals.sort()
        # set the return list appended with the first interval
        ans = [intervals[0]]
        # iterate through the intervals
        for interval in intervals[1:]:
            # if the previous interval does not overlap with the current interval
            if ans[-1][1] < interval[0]:
                # append to the return list
                ans.append(interval)
            # if the previous interval overlaps with the current interval
            else:
                # merge the current interval with the previous interval
                ans[-1][1] = max(ans[-1][1], interval[1])
        # return the result
        return ans