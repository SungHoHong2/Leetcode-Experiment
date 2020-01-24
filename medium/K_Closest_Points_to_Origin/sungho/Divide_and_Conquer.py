class Solution(object):
    def kClosest(self, points, K):
        def findK(Points, K):

            # if K is zero return empty Array
            if K == 0:
                return []

            # if array of the points is smaller than K
            if len(Points) <= K:
                # return the location into the array
                return [p[1] for p in Points]

            # get the pivot as the distance of the first array
            pivot, left, right = Points[0], [], []

            # iterate the points
            for p in Points:
                # if the distance is bigger than the pivot
                if p[0] > pivot[0]:
                    # append it to the right array
                    right.append(p)

                # if the distance is smaller than the pivot
                elif p[0] < pivot[0]:
                    # append it to the left array
                    left.append(p)

            # if the left array is bigger or same as the K
            if len(left) >= K:

                # find more in the left array
                return findK(left, K)

            # if left is smaller than the K
            else:
                # return rest of the left array + pivot + the rest in the right array
                return [l[1] for l in left] + [pivot[1]] + findK(right, K - 1 - len(left))

        # create the array that consists of (distance, (x,y))
        # start the divide and conquer
        return findK([[p[0] ** 2 + p[1] ** 2, p] for p in points], K)