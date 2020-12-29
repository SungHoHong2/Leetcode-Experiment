class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # set up the dictionary to track the index of complements
        memory = dict()
        # loop through the array
        for i in range(0, len(nums)):
            # get the complement from subtracting the items from target.
            complement = target - nums[i]

            # if the complement does not exist
            if complement not in memory:
                # add the current item to the dictionary
                memory[nums[i]] = i
            else:
                # return if the complement matches with the item in the dictionary
                return [memory[complement], i]