class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        t = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)

        t.append(t[0] + 1440)

        return min(b - a for a, b in zip(t[:-1], t[1:]))