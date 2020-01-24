class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        def find(Points, K):
            if K == 0:
                return []
            if K >= len(Points):
                return [p[1] for p in Points]
            pivot = Points[0]
            left = []
            right = []
            for p in Points:
                if p[0] > pivot[0]:
                    right.append(p)
                elif p[0] < pivot[0]:
                    left.append(p)

            if len(left) >= K:
                return find(left, K)
            else:
                return [l[1] for l in left] + [pivot[1]] + find(right, K - 1 - len(left))

        Points = [[p[0] ** 2 + p[1] ** 2, p] for p in points]
        return find(Points, K)
