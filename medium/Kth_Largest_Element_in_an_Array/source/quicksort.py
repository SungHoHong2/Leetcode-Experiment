class Solution:
    def findKthLargest(self, nums, k):

        def partition(left, right):
            # find the random pivot index and the value
            pivot_index = random.randint(left, right)
            # get the value of the pivot
            pivot_value = nums[pivot_index]
            # temporary hide the pivot value in the rightmost side
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            # move all smaller values to the leftside
            middle = left
            for i in range(left, right):
                if nums[i] < pivot_value:
                    nums[middle], nums[i] = nums[i], nums[middle]
                    middle += 1
            # recover the pivot value from the rightmost side
            nums[right], nums[middle] = nums[middle], nums[right]
            # return the index of the pivot
            return middle

        def qsort(left, right, K):
            # return the item if the recursion reach the leaf
            if left == right:
                return nums[left]
            # get the index of the pivot from the partition
            mid = partition(left, right)
            # if the index of the pivot is the Kth smallest
            if K == mid:
                # return the value
                return nums[K]
            # if pivot is bigger than the kth smallest
            elif mid > K:
                # search the leftside
                return qsort(left, mid - 1, K)
            # if the pivot is smaller than the kth smallest
            elif mid < K:
                # search the rightside
                return qsort(mid + 1, right, K)

        # return the kth largest value from the quicksort
        return qsort(0, len(nums) - 1, len(nums) - k)