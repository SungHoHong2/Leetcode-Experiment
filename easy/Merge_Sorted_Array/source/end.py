class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1
        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            # if tail of the nums1 is smaller than the tail of the nums2
            if nums1[p1] < nums2[p2]:
                # append nums2 tail first
                nums1[p] = nums2[p2]
                # decrease the index
                p2 -= 1
            else:
                # append nums1 tail first
                nums1[p] = nums1[p1]
                # decrease the index of nums1
                p1 -= 1
            p -= 1
        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]