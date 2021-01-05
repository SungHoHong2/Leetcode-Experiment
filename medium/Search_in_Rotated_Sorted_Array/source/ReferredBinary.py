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
            if nums[start] <= nums[mid] :
                # search the leftside if target is in the leftside
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                # search rightside if target is in the rightside
                else:
                    start = mid + 1
            # no rotation found between middle and end
            else:
                # search rightside if the target is in the rightside
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                # search leftside if the target is in the leftside
                else:
                    end = mid - 1
        # return -1 if no target is found in the array
        return -1