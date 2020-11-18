class Solution(object):
    def kClosest(self, points, K):
        # create a lambda function that calculates the euclidean distance
        dist = lambda i: sqrt(points[i][0] ** 2 + points[i][1] ** 2)

        def sort(i, j, K):
            # return when recursion tree reaches the leaf
            if i >= j: return
            # find the random pivot index
            k = random.randint(i, j)
            # place the pivot in the front of the array
            points[i], points[k] = points[k], points[i]
            # parition the index based on the random pivot and get the pivot index
            mid = partition(i, j)
            # if the number of elements in the leftside is more than K
            if K < mid - i + 1:
                # sort recursively from the left array
                sort(i, mid - 1, K)
            # if the number of elements of the left side is less than K
            elif K > mid - i + 1:
                # explore more elements in the right side just enough to match the K
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # save the pivot index
            oi = i
            # get the distance of the pivot
            pivot = dist(i)
            # quick-sort the elements using the pivot
            i += 1
            while True:
                # increment from left if the distance is smaller than the pivot's
                while i < j and dist(i) < pivot:
                    i += 1
                # decrement from right if the distance is larger than the pivot's
                while i <= j and dist(j) >= pivot:
                    j -= 1
                # break if the sorting is complete
                if i >= j: break
                # swap the incompatible distances between left and right
                points[i], points[j] = points[j], points[i]
            # swap the pivot with the recently swapped leftside distance
            points[oi], points[j] = points[j], points[oi]
            # return middle index
            return j

        # invoke sort function
        sort(0, len(points) - 1, K)
        # return the kth amount of sorted result
        return points[:K]