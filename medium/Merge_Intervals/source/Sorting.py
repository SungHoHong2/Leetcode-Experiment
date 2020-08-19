class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals based the starting point
        intervals.sort(key=lambda x: x[0])
        # set the return list
        merged = []
        # iterate through the intervals
        for interval in intervals:
            # if it is the first interval or the previous interval does not overlap with the current interval
            if not merged or merged[-1][1] < interval[0]:
                # append to merge
                merged.append(interval)
            # if it s not the first interval and the previous interval overlaps with the current interval
            else:
                # merge the current interval with the previous interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        # return the result
        return merged