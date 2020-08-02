class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # make a copy of nums1
        _nums1 = nums1[:m]
        # empty the nums1(return array)
        nums1[:] = [None for i in nums1]
        # get pointers for nums1, nums2 and return array.
        i = j = k = 0
        # iterate until the nums1 or the num2 are empty
        while i < m and j < n:
            # if nums1 is smaller
            if _nums1[i] < nums2[j]:
                # append nums1 to return array
                nums1[k] = _nums1[i]
                # increaese the index of nums1
                i += 1
            # if nums2 is smaller
            else:
                # append nums2 to return array
                nums1[k] = nums2[j]
                # increase the index of nums2
                j += 1
            # increase the indes of the return array
            k += 1
        # if nums1 is not empty
        while i < m:
            # append nums1 to the return array
            nums1[k] = _nums1[i]
            i += 1
            k += 1
        # if nums2 is not empty
        while j < n:
            # append nums2 to the return array
            nums1[k] = nums2[j]
            j += 1
            k += 1
