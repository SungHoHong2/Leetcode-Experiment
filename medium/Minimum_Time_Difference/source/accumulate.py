class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # sort the timepoints according to the total accumulated minutes
        t = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        # append the first timepoint that starts after 24 hours
        t.append(t[0] + 1440)
        # compare the difference of intervals of timepoints
        return min(b - a for a, b in zip(t[:-1], t[1:]))