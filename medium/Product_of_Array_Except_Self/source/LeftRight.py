class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initiate the left, right and return array
        left = [0 for i in nums]
        right = [0 for i in nums]
        answer = [0 for i in nums]
        # Aggregate the products from the left
        left[0] = 1
        for i in range(1, len(nums)):
            # track the history of the aggregated product until one element is left in the nums array
            left[i] = nums[i - 1] * left[i - 1]
        # Aggregate the products from the left
        right[len(nums) - 1] = 1
        for i in reversed(range(len(nums) - 1)):
            # track the history of the aggregated product until one element is left in the nums array
            right[i] = nums[i + 1] * right[i + 1]
        # Calculate the product that excludes the original element in the nums array
        for i in range(len(nums)):
            # calculate the products of the left and the right calculation
            answer[i] = left[i] * right[i]
        # return the answer
        return answer