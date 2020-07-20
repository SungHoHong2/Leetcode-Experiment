class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax = 0
        currMax = 0

        # avoids summing up adjacent numbers
        for x in nums:
            # save the previous currMax
            temp = currMax

            # aggregate x from preMax and generate new currMax
            currMax = max(prevMax + x, currMax)

            # update the premax with the previous currMax
            prevMax = temp

        return currMax
