class Solution(object):
    def kClosest(self, points, K):
        def dist(i):
            return pow(points[i][0], 2) + pow(points[i][1], 2)

        def sort(left, right, K):
            # return when recursion tree reaches the leaf
            if left >= right:
                return
                # parition the index based on the random pivot and get the pivot index
            mid = partition(left, right)
            # get the sorted length
            sorted_total = (mid - left + 1)
            # if the sorted result is more than K
            if sorted_total > K:
                # reduce the scope of the return by sorting out the left side of the input
                sort(left, mid - 1, K)
            # if the sorted result is less than K
            else:
                # increase the scope of the return by sorting the right side of the input
                sort(mid + 1, right, K - sorted_total)
            pass

        def partition(left, right):
            # find the random pivot index
            pivot = random.randint(left, right)
            # place the pivot in the front of the array
            points[left], points[pivot] = points[pivot], points[left]
            # set the pivot and the left index
            pivot, left = left, left + 1
            # quick-sort the elements using the pivot
            while True:
                # increment from left if the distance is smaller than the pivot's
                while left < right and dist(left) < dist(pivot):
                    left += 1
                    # decrement from right if the distance is larger than the pivot's
                while left <= right and dist(pivot) <= dist(right):
                    right -= 1
                    # break if the sorting is complete
                if left >= right:
                    break
                # swap the incompatible distances between left and right
                points[left], points[right] = points[right], points[left]
            # swap the pivot with the recently swapped leftside distance
            points[pivot], points[right] = points[right], points[pivot]
            # return middle index
            return right

            # invoke sort function

        sort(0, len(points) - 1, K)
        # return the kth amount of sorted result
        return points[:K]