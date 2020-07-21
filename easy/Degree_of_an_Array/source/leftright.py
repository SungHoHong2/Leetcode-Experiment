class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        # create three dictionary
        left, right, count = {}, {}, {}

        # iterate the numbers
        for i, x in enumerate(nums):

            # record the leftmost index of the repeated char
            if x not in left: left[x] = i

            # record the rightmost index of the repeated char
            right[x] = i

            # count the number of repeated chars
            count[x] = count.get(x, 0) + 1

        # set up the least length
        ans = len(nums)

        # get the most repeated char
        degree = max(count.values())

        # iterate the counts of the repeated numbers
        for x in count:
            # if the repeated number is the most repeated
            if count[x] == degree:
                # calculate the length of the substring
                ans = min(ans, right[x] - left[x] + 1)

        # return the ans
        return ans
