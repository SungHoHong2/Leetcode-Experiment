class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(left, right, pivot_index):
            # get the value of the pivot
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            # 2. move all smaller values to the leftside
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]
            # return the index of the pivot
            return store_index

        def select(left, right, k_smallest):
            # return the item if the recursion reach the leaf
            if left == right:
                return nums[left]
                # select a random pivot_index between
            pivot_index = random.randint(left, right)
            # get the index of the pviot from the partition
            pivot_index = partition(left, right, pivot_index)
            # if the index of the pivot is the Kth smallest
            if k_smallest == pivot_index:
                # return the value
                return nums[k_smallest]
            # if pivot is bigger than the kth smallest
            elif k_smallest < pivot_index:
                # search the leftside
                return select(left, pivot_index - 1, k_smallest)
            # if the pivot is smaller than the kth smallest
            else:
                # serach the rightside
                return select(pivot_index + 1, right, k_smallest)

        # invoke the recursion [ kth largest = (n - k)th smallest ]
        return select(0, len(nums) - 1, len(nums) - k)