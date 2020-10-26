class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create a set for return value and checking for duplicates
        res, dups = set(), set()
        # iterate the numbers
        for i in range(len(nums)):
            # if the variable are not in the duplicate
            if nums[i] not in dups:
                # create a hashmap
                cache = set()
                # add the variable in the hashset
                dups.add(nums[i])
                # iterate the rightside array of the current element
                for left in range(i+1, len(nums)):
                    # calculate the complement
                    complement = 0 - nums[i] - nums[left]
                    # if the complement is in the hashmap and it is part of the current index
                    if complement in cache:
                        # add the results(fix the orders because the answer may append duplicates)
                        res.add(tuple(sorted((nums[i], nums[left], complement))))
                    # add the leftmost value in the hashmap and the current index as the key
                    cache.add(nums[left])
        # return the array
        return res