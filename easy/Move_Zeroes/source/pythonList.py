class Solution:

    def moveZeroes(self, nums: List[int]) -> None:

        start, end = 0, len(nums)
        while start < end:

            # if the current element is zero
            if nums[start] == 0:
                # move the element to the last
                nums.pop(start)
                nums.append(0)
                # reduce the final length
                end -= 1

                # if the current element is not zero
            else:
                # move on to the next element
                start += 1