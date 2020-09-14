class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set up the start pointer for binary search
        start = 0
        # set up the end pointer for binary search
        end = len(nums) - 1
        # loop until the array is completely explored
        while start <= end:
            # get the pivot
            mid = start + (end - start) // 2
            # if the pivot is the target
            if nums[mid] == target:
                # return the index of the pivot
                return mid
            # implies no rotation in the array
            if nums[mid] >= nums[start]:
                #  S     M     E
                # [0,1,2,3,4,5,6]
                # if the target is smaller than the pivot
                # Target = 1
                if nums[start] <= target < nums[mid]:
                    # search the left side of the array
                    end = mid - 1
                # if the target is bigger than the pviot
                # Target = 5
                else:
                    # search the right side of the array
                    start = mid + 1
            # implies a rotation in the array
            else:
                #  S     M     E
                # [4,5,6,0,1,2,3]
                # if the target is larget than the middle
                # Target = 1
                if nums[mid] < target <= nums[end]:
                    # search the right side of the array
                    start = mid + 1
                # if the target is smaller than the middle
                # Target = 5
                else:
                    # search the left side of the array
                    end = mid - 1
        # return -1 if no target is found in the array
        return -1
