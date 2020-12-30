class Solution:

    def twoSum(self, nums, i, target, res):
        # create a hashset for complements
        cache = set()
        # iterate from left to right
        for left in range(i + 1, len(nums)):
            # calculate the complement
            complement = target - nums[i] - nums[left]
            # if the complement is in the hashset
            if complement in cache:
                # add the results(fix the orders because the answer may append duplicates)
                res.add(tuple(sorted([nums[i], complement, nums[left]])))
            # record the complement if the complement is not in the hashset
            else:
                cache.add(nums[left])

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create sets for return value and checking for duplicates
        res, dups = set(), set()
        # iterate the each number and run twoSum function
        for i in range(len(nums)):
            # run twoSum only on nonduplicates
            if nums[i] not in dups:
                # record the duplicates in the set
                dups.add(nums[i])
                # invoke the twoSum function
                self.twoSum(nums, i, 0, res)
        # return the collections that sum up to zero
        return res

