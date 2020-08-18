class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initiate the return array
        answer = [1 for i in nums]
        # Aggregate the products from the left
        left = 1
        for i in range(len(nums)):
            answer[i] = answer[i] * left
            left *= nums[i]
        # Aggregate the products from the right
        right = 1
        for i in reversed(range(len(nums))):
            answer[i] = answer[i] * right
            right *= nums[i]
        # return the answer
        return answer