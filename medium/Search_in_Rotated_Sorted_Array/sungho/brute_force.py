class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # print(nums, target)
        for i in range(0, len(nums)):
            if target == nums[i]:
                return i

        return -1