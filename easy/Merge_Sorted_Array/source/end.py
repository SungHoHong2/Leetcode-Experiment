class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # two get pointers for nums1 and nums2
        i = m - 1
        j = n - 1
        # set pointer for nums1
        k = m + n - 1
        # while there are still elements to compare
        while i >= 0 and j >=0:
            # if tail of the nums1 is smaller than the tail of the nums2
            if nums1[i] < nums2[j]:
                # append nums2 tail first
                nums1[k] = nums2[j]
                # decrease the index
                j -= 1
            # if the tail of the nums2 is smaller than the nums1
            else:
                # append nums1 tail first
                nums1[k] = nums1[i]
                # decrease the index of nums1
                i -=1
            # decrease the index of the return array
            k -=1
        # add missing elements from nums2
        nums1[:j + 1] = nums2[:j + 1]