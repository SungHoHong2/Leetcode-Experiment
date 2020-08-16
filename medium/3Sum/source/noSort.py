class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create a set for return value and checking for duplicates
        res, dups = set(), set()
        # create a hashmap
        seen = {}
        # iterate the numbers
        for i in range(len(nums)):
            # if the variable are not in the duplicate
            if nums[i] not in dups:
                # add the variable in the hashset
                dups.add(nums[i])
                # iterate the rightside array of the current element
                for j in range(i+1, len(nums)):
                    # calculate the complement
                    complement = 0 - nums[i] - nums[j]
                    # if the complement is in the hashmap and it is part of the current index
                    if complement in seen and seen[complement] == i:
                        # add the results(fix the orders because the answer may append duplicates)
                        res.add(tuple(sorted((nums[i], nums[j], complement))))
                    # add the leftmost value in the hashmap and the current index as the key
                    seen[nums[j]] = i
        # return the array
        return res