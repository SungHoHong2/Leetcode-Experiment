class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find_rotate_index(left, right):

            # if first element is smaller than the last element
            if nums[left] < nums[right]:
                # first element is the smallest
                return 0

            # if there was some rotation
            while left <= right:

                # get the middle pivot
                pivot = (left + right) // 2

                # if the pivot is larger than the right neighbor
                #            | |
                # ex) [4,5,6,7,0,1,2]
                # return the index of the right side
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1

                # if the pivot is smaller than the right neighbor
                # continue searching for the rotation point
                # if the pivot is smaller than the left side
                if nums[pivot] < nums[left]:
                    # search for the left area
                    right = pivot - 1

                # if the pviot is larger than the left side
                # search for the right area
                else:
                    left = pivot + 1

        def search(left, right):
            """
            Binary search
            """

            while left <= right:

                # divide the search area to left and right
                pivot = (left + right) // 2

                # if the pivot is the one looking for
                if nums[pivot] == target:
                    return pivot

                # if the pivot is larger than the target
                if target < nums[pivot]:
                    # search the left area
                    right = pivot - 1

                # if the pivot is smaller than the target
                else:
                    # search for the right area
                    left = pivot + 1
            return -1

        n = len(nums)

        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_index = find_rotate_index(0, n - 1)

        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index

        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search(0, n - 1)

        # ex) [4,5,6,7,0,1,2]
        #     target = 3
        #     makes sense to search from the other half
        if target < nums[0]:
            # search on the right side
            return search(rotate_index, n - 1)

        # ex) [4,5,6,7,0,1,2]
        #     target = 6
        # search on the left side
        return search(0, rotate_index)



