class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # The length of the input array
        length = len(nums)
        # The left and right arrays
        L, R, answer = [0] * length, [0] * length, [0] * length
        # Aggregate the products from the left
        L[0] = 1
        for i in range(1, length):
            # track the history of the aggregated product until one element is left in the nums array
            L[i] = nums[i - 1] * L[i - 1]
        # Aggregate the products from the left
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            # track the history of the aggregated product until one element is left in the nums array
            R[i] = nums[i + 1] * R[i + 1]
        # Calculate the product that excludes the original element in the nums array
        for i in range(length):
            # calculate the products of the left and the right calculation
            answer[i] = L[i] * R[i]
        # return the answer
        return answer