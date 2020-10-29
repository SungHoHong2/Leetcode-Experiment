class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # search from the smallest array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        # get the length of array x
        x = len(nums1)
        # get the length of array y
        y = len(nums2)
        # set the low and high pointer for binary search in array x
        low, high = 0, x
        # invoke the binary search
        # x [       maxLeft | minRight     ]
        # y [                 maxLeft | minRight     ]
        while low <= high:
            # get the length of the partition of array x
            partitionX = (low + high) // 2
            # get the length of the partition of array y that is same as partition of array x
            # ex) the less items in array x, more items need to go to array y
            partitionY = (x+y+1) // 2 - partitionX
            # update the index for left partition
            maxLeftX = float("-inf") if partitionX == 0 else nums1[partitionX-1]
            maxLeftY = float("-inf") if partitionY == 0 else nums2[partitionY-1]
            # update the index for right partition
            minRightX = float("inf") if partitionX == x else nums1[partitionX]
            minRightY = float("inf") if partitionY == y else nums2[partitionY]
            # partitioned the array at the correct place
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # return the result when the length of the whole array is even
                if (x+y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
                # return the result when the length of the whole array is odd
                else:
                    return max(maxLeftX, maxLeftY)
            # shrink the leftside partition
            elif maxLeftX > minRightY:
                high = partitionX - 1
            # shrink the rightside partition
            else:
                low = partitionX + 1