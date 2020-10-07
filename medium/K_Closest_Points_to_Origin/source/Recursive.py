class Solution(object):
    def kClosest(self, points, K):
        # create a function that calculates the euclidean distance
        dist = lambda i: sqrt(points[i][0] ** 2 + points[i][1] ** 2)

        def sort(i, j, K):
            # return when recursion tree reaches the leaf
            if i >= j: return
            # get the random index between ith and jth index
            k = random.randint(i, j)
            # swap the values in the array
            points[i], points[k] = points[k], points[i]
            # return the partitioned index A[i] <= A[mid] <= A[j] for i < mid < j.
            mid = partition(i, j)
            # if the number of Kth element is smaller than the partitioned index
            if K < mid - i + 1:
                # sort again in the left array
                sort(i, mid - 1, K)
            # if the number of kth element is bigger than the partitioned index
            elif K > mid - i + 1:
                # sort again in the right array
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # set the orgiinal i
            oi = i
            # get the distance of the random pivot
            pivot = dist(i)
            i += 1
            # loop until middle index is found
            while True:
                # increment left index until the current distance reaches the pivot
                while i < j and dist(i) < pivot:
                    i += 1
                # decrement right index until the current distance reaches the pivot
                while i <= j and dist(j) >= pivot:
                    j -= 1
                # break when i and j meets
                if i >= j: break
                # swap the ith and jth index to prevent looping forever
                points[i], points[j] = points[j], points[i]
            # swap back the original index and the jth index
            points[oi], points[j] = points[j], points[oi]
            # return jth index
            return j

        # invoke sort function
        sort(0, len(points) - 1, K)
        # return the kth amount of sorted result
        return points[:K]