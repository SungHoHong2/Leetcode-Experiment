class Solution(object):
    def kClosest(self, points, K):
        # create a lambda function that calculates the euclidean distance
        dist = lambda i: sqrt(points[i][0]**2 + points[i][1]**2)

        def sort(i, j, K):
            # return when recursion tree reaches the leaf
            if i >= j: return
            # get the pivot index that will sort array A[ i...pivot...j ]
            k = random.randint(i, j)
            # place the pivot in the front of the array A[ pivot.i....j ]
            points[i], points[k] = points[k], points[i]
            # return the partitioned index A[i] <= A[mid] <= A[j]
            mid = partition(i, j)
            # if the number of Kth element is smaller than the partitioned index
            if K < mid - i + 1:
                # sort recursively from the left array
                sort(i, mid - 1, K)
            # if the number of kth element is bigger than the partitioned index
            elif K > mid - i + 1:
                # sort recursively from the right array
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # save the pivot index
            oi = i
            # get the distance value of the pivot
            pivot = dist(i)
            # move to the index that needs to be sorted
            i += 1
            # loop until the sorting is complete
            while True:
                # increment from left if the distance of ith index is smaller than the pivot
                while i < j and dist(i) < pivot:
                    i += 1
                # increment from right if the distance of ith index is bigger than the pivot
                while i <= j and dist(j) >= pivot:
                    j -= 1
                # break if the sorting is complete
                if i >= j: break
                # place the smaller value to the leftside and bigger value to the rigtside of the pivot
                points[i], points[j] = points[j], points[i]
            # move the pivot value to the middle index
            points[oi], points[j] = points[j], points[oi]
            # return middle index
            return j

        # invoke sort function
        sort(0, len(points) - 1, K)
        # return the kth amount of sorted result
        return points[:K]