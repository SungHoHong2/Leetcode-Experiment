class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # set the two indexs from left and right
        left = 0
        right = len(numbers) - 1
        # loop until the two pointers converge
        while left < right:
            # calculate the sum of the leftmost and the rightmost value
            sum = numbers[left] + numbers[right]
            # if the results are equal to the target
            if sum == target:
                # return the indexes
                return [left + 1, right + 1]
            # if the results are smaller than the target
            elif sum < target:
                # increase the leftmost pointer
                left += 1
                # if the results are bigger than the target
            else:
                # decrease the rightmost pointer
                right -= 1
        # return [-1,-1] if there is no match
        return [-1, -1]

