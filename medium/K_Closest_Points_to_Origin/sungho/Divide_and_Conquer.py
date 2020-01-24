class Solution(object):
    def kClosest(self, points, K):
        def findK(Points, K):
            if K == 0:
                return []
            if len(Points) <= K:
                return [p[1] for p in Points]

            pivot, left, right = Points[0], [], []
            for p in Points:
                if p[0] > pivot[0]:
                    right.append(p)
                elif p[0] < pivot[0]:
                    left.append(p)

            if len(left) >= K:
                return findK(left, K)
            else:
                return [l[1] for l in left] + [pivot[1]] + findK(right, K - 1 - len(left))


        Points = [[p[0] ** 2 + p[1] ** 2, p] for p in points]
        return findK(Points, K)