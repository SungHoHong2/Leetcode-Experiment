class Solution:
    def find_rotate_index(self, nums, left, right):
        # if first element is smaller than the last element
        if nums[left] < nums[right]:
            # there was no rotation in the array
            return 0
        # loop until the whole array is searched
        while left <= right:
            # get the middle pivot
            pivot = (left + right) // 2
            # if the pivot is larger than the rightside neighbor
            #            P N
            # ex) [4,5,6,7,0,1,2]
            if nums[pivot] > nums[pivot + 1]:
                # return the index of the right side
                return pivot + 1
            # if the pivot is smaller than the left side
            #            L   P   R
            # ex) [4,5,6,7,0,1,2,3]
            if nums[pivot] < nums[left]:
                # search for the left area
                right = pivot - 1
            # if the pivot is larger than the left side
            #        L   P   R
            # ex) [4,5,6,7,0,1,2,3]
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
            if target < nums[pivot]:
                # search the left area of the array
                right = pivot - 1
            # if the pivot is smaller than the target
            else:
                # search for the right area of the array
                left = pivot + 1
        # return -1 if there is no target in the array
        return -1

    def search(self, nums, target):
        # get the total length of
        n = len(nums)
        # if there are no numbers
        if n == 0:
            # return -1
            return -1
        # if there is a single number
        if n == 1:
            # return zero if the single number matches with the target otherwise -1
            return 0 if nums[0] == target else -1
        # find the smallest elemement in the array = rotate_index
        rotate_index = self.find_rotate_index(nums, 0, n - 1)
        # if target is the smallest element
        if nums[rotate_index] == target:
            # return the rotate_index
            return rotate_index
        # if array is not rotated
        if rotate_index == 0:
            # perform binary search on the entire array
            return self.binarySearch(nums, target, 0, n - 1)
        # if the target is smaller than the first element
        # ex) [4,5,6,7,0,1,2]
        #     target = 2 first = 4
        if target < nums[0]:
            # search from the rotate_index
            return self.binarySearch(nums, target, rotate_index, n - 1)
        # if the target is bigger than the first element
        # ex) [4,5,6,7,0,1,2]
        #     target = 6 first = 4
        # search until the rotate_index
        return self.binarySearch(nums, target, 0, rotate_index)

