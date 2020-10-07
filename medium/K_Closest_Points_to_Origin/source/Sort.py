class Solution(object):
    def kClosest(self, points, K):
        # sort the array based on the euclidean distance
        points.sort(key = lambda P: sqrt(P[0]**2 + P[1]**2))
        # return the kth amount of the list
        return points[:K]