class Solution(object):

    # define a recursive merge sort
    def mergeSort(self, arr):

        # if the array is more than one lement
        if len(arr) > 1:
            # find the middle of the array
            mid = len(arr) // 2
            # create a temporary left array
            L = arr[:mid]
            # create a temporary right array
            R = arr[mid:]
            # run recursive for the left array
            self.mergeSort(L)
            # run recursive for the right array
            self.mergeSort(R)
            # set the index for left array, right array and return array
            i = j = k = 0
            # loop until left or right is depleted
            while i < len(L) and j < len(R):
                # if left is smaller than right
                if L[i] < R[j]:
                    # left goes to the return array
                    arr[k] = L[i]
                    # increase the index of the left
                    i += 1
                # if right is smaller than
                else:
                    # right goes to the return array
                    arr[k] = R[j]
                    j += 1
                # increase the index of the return array
                k += 1

            # empty the left array
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            # empty the right array
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # append the array
        nums1[:] = nums1[:m] + nums2[:n]
        self.mergeSort(nums1)
