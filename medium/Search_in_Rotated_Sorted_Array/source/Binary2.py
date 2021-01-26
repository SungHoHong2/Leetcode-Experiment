class Solution:
    def find_rotate_index(self, nums, left, right):
        # if first element is smaller than the last element
        if nums[0] < nums[-1]:
            # there was no rotation in the array
            return 0
            # loop until the whole array is searched
        while left <= right:
            # get the middle pivot
            pivot = (left + right) // 2
            # if the rightside of the pivot is the rotated index
            if nums[pivot] > nums[pivot + 1]:
                # return the index of the right side
                return pivot + 1
                # if the pivot is in the rightside of the rotated index
            if nums[pivot] < nums[left]:
                # search for the left area
                right = pivot - 1
                # if the pivot is in the leftside of the rotated index
            else:
                # search for the right area
                left = pivot + 1

    def binarySearch(self, nums, target, left, right):
        # loop until the whole array is searched
        while left <= right:
            # get the middle pivot
            pivot = (left + right) // 2
            # if the pivot matches the target
            if nums[pivot] == target:
                # return the pivot
                return pivot
            # if the pivot is larger than the target
            if nums[pivot] > target:
                # search the left area of the array
                right = pivot - 1
            # if the pivot is smaller than the target
            else:
                # search for the right area of the array
                left = pivot + 1
        # return -1 if there is no target in the array
        return -1

    def search(self, nums, target):
        # get the total length of nums
        n = len(nums)
        # return -1 if there are no numbers
        if n == 0:
            return -1
            # if there is a single number
        if n == 1:
            # return zero if the single number matches with the target otherwise -1
            return 0 if nums[0] == target else -1
            # find the rotate_index in the array = rotate_index
        rotate_index = self.find_rotate_index(nums, 0, n - 1)
        # if target is the rotate_index
        if target == nums[rotate_index]:
            # return the rotate_index
            return rotate_index
        # if array is not rotated
        if rotate_index == 0:
            # perform binary search on the entire array
            return self.binarySearch(nums, target, 0, n - 1)
        # if the target is in the rightside of the rotated array
        if target < nums[0]:
            # search from the rotate_index
            return self.binarySearch(nums, target, rotate_index, n - 1)
        # search the leftside of the rotated array
        return self.binarySearch(nums, target, 0, rotate_index)