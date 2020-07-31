class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # make a copy of nums1
        nums1_copy = nums1[:m]
        # empty the nums1(return array)
        nums1[:] = []
        # Two get pointers for nums1 and nums2.
        p1 = 0
        p2 = 0
        # iterate until the nums1 or the num2 are empty
        while p1 < m and p2 < n:
            # if nums1 is smaller
            if nums1_copy[p1] < nums2[p2]:
                # append nums1 to return array
                nums1.append(nums1_copy[p1])
                # increaese the index of nums1
                p1 += 1
            # if nums2 is smaller
            else:
                # append nums2 to return array
                nums1.append(nums2[p2])
                # increase the index of nums2
                p2 += 1
        # if nums1 is not empty
        if p1 < m:
            # append nums1 to the return array
            nums1[p1 + p2:] = nums1_copy[p1:]
        # if nums2 is not empty
        if p2 < n:
            # append nums2 to the return array
            nums1[p1 + p2:] = nums2[p2:]