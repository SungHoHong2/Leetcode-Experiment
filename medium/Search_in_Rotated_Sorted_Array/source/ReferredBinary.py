class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set up the start pointer for binary search
        start = 0
        # set up the end pointer for binary search
        end = len(nums) - 1
        # loop until the array is completely explored
        while start <= end:
            # get the pivot
            mid = (start + end) // 2
            # if the pivot is the target
            if nums[mid] == target:
                # return the index of the pivot
                return mid
            # no rotation found between start and middle
            if nums[mid] >= nums[start]:
                # if target is in the leftside (small to medium)
                if nums[start] <= target < nums[mid]:
                    # search the left side of the array
                    end = mid -1
                # if target is in the rightside (note that we cannot compare with size because there may be a rotation)
                else:
                    # search the rightside
                    start = mid + 1
            # rotation found between start and middle
            else:
                # if the target is in the rightside (small to medium)
                if nums[mid] < target <= nums[end]:
                    # search the right side of the array
                    start = mid + 1
                # if the target is in the leftside
                else:
                    # search the leftside
                    end = mid -1
        # return -1 if no target is found in the array
        return -1