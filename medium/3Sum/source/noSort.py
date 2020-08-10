class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create a set for return value and checking for duplicates
        res, dups = set(), set()
        # create a hashmap
        seen = {}
        # iterate the numbers
        for i, val1 in enumerate(nums):
            # if the variable are not in the duplicate
            if val1 not in dups:
                # add the variable in the hashset
                dups.add(val1)
                # iterate the rightside array of the current element
                for j, val2 in enumerate(nums[i+1:]):
                    # calculate the complement
                    complement = -val1 - val2
                    # if the complement is in the hashmap and it is part of the current index
                    if complement in seen and seen[complement] == i:
                        # add the results(fix the orders because the answer may append duplicates)
                        res.add(tuple(sorted((val1, val2, complement))))
                    # add the leftmost value in the hashmap and the current index as the key
                    seen[val2] = i
        # return the array
        return res