class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            # set a list that stores the group of four integers that sums up to the target
            res = []
            # return the empty list if there is no more input
            if len(nums) == 0:
                return res
                # return empty list if the k number of smallest or largest values cannot match the target
            if nums[0] * k > target or target > nums[-1] * k:
                return res
            # invoke the twoSum function if 2 numbers need to match the target
            if k == 2:
                return twoSum(nums, target)
            # iterate the index
            for i in range(len(nums)):
                # if it is the first index or not duplicated
                if i == 0 or nums[i - 1] != nums[i]:
                    # append the current number with the the recursion using reduced target and k number
                    for set in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            # set a return list
            res = list()
            # set a left and right
            left, right = 0, len(nums) - 1
            # loop until left and right converge
            while (left < right):
                # compute the sum of left and right
                sum = nums[left] + nums[right]
                # move left to right if the sum is smaller than the target
                if sum < target:
                    left += 1
                # move right to left if the sum is bigger than the target
                elif sum > target:
                    right -= 1
                # append the answer if the sum is equal
                else:
                    res.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                # skip the duplicated inputs
                while left < right and nums[left - 1] == nums[left]:
                    left += 1
            # return the collection of answers
            return res

        # sort the input in ascending order
        nums.sort()
        # invoke the recursion
        return kSum(nums, target, 4)