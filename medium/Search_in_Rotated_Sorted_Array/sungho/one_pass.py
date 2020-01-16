class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:

            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid

            # if the pivot is not the target
            # if the pivot is larger than the left
            elif nums[mid] >= nums[start]:

                # If the target is bigger than the start and smaller than pivot
                if target >= nums[start] and target < nums[mid]:
                    # search for the left side
                    end = mid - 1
                else:
                    # search for the right side
                    start = mid + 1
            else:
                # If the target is smaller than the end AND larger than the pivot
                if target <= nums[end] and target > nums[mid]:
                    # search for the right side
                    start = mid + 1
                else:
                    # if not search for the left side
                    end = mid - 1

        # nothing fount return NULL
        return -1