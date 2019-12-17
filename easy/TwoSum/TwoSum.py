# 1. Two Sum
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]

from typing import List, Dict

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print(nums, target)

        # brute force solution

        # loop through all the numbers that have the same value as the target
        for i in range(0, len(nums)-1):
            # avoid traversing the items that have already been compared
            for s in range(i+1, len(nums)):
                print(nums[i], nums[s], nums[i] + nums[s])
                if (nums[i] + nums[s]) == target:
                    # if the result is equal to the target return
                    print("target found")
                    return [i, s]
        return False

    def twoPathHash(self, nums: List[int], target: int) -> List[int]:

        # create a dictionary
        hashmap = {}

        # loop through the array
        for i in range(0, len(nums)):
            # get the complement from subtracting the items from target.
            complement = target-nums[i]

            # if the complement does not exist
            if complement not in hashmap:
                # add the current item to the dictionary
                hashmap[nums[i]] = i
            else:
                print([hashmap[complement],i])
                # return if the complement matches with the item in the dictionary
                return[hashmap[complement],i]


def main():
    arg1 = [2,7,11,15]
    # arg1 = [-1,-2,-3,-4,-5_Longest_Common_Prefix]
    arg2 = 9
    # arg2 = -8

    # Brute Force solution
    # return Solution().twoSum(arg1,arg2)
    return Solution().twoPathHash(arg1,arg2)

if __name__ == "__main__":
    main()

