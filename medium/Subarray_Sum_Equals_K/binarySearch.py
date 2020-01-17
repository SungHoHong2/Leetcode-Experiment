class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) / 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        minimum = start
        print minimum
        if nums[minimum] == target:
            return minimum
        start = minimum if target <= nums[len(nums) - 1] else 0
        end = minimum if target > nums[len(nums) - 1] else len(nums) - 1

        while start <= end:
            mid = start + (end - start) / 2

            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return -1