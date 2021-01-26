class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set up the left and right pointer for binary search
        left, right = 0, len(nums) - 1
        # loop until the array is completely explored
        while left <= right:
            # get the pivot
            pivot = (left + right) // 2
            # return the pivot if the pivot is the target
            if nums[pivot] == target:
                return pivot
            # if no rotation found between start and middle
            if nums[left] <= nums[pivot]:
                # search the leftside if target is in the rotation free array
                if nums[left] <= target < nums[pivot]:
                    right = pivot -1
                # search rightside if target is in the array that contains rotation
                else:
                    left = pivot + 1
            # if no rotation found between middle and end
            else:
                # search rightside if the target in the rotation free array
                if nums[pivot] < target <= nums[right]:
                    left = pivot + 1
                # search leftside if the target is in the array that contains rotation
                else:
                    right = pivot - 1
        # return -1 if no target is found in the array
        return -1