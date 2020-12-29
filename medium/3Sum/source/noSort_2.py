class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create a set for return value and checking for duplicates
        res, dup = set(), set()
        # iterate the numbers
        for i in range(len(nums)):
            # if the variable are not in the duplicate
            if nums[i] not in dup:
                # create a hashmap for complements
                cache = set()
                # record the duplicate in the hashset
                dup.add(nums[i])
                # iterate the rightside array of the current element
                for left in range(i+1, len(nums)):
                    # calculate the complement
                    complement = 0 - nums[i] - nums[left]
                    # if the complement is in the hashmap
                    if complement in cache:
                        # add the results(fix the orders because the answer may append duplicates)
                        res.add(tuple(sorted([nums[i], nums[left], complement])))
                    # add the leftmost value as the future complement in the hashmap
                    cache.add(nums[left])
        # return the answers
        return res