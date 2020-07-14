class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rtnArr = list()

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    rtnArr.append(i)
                    rtnArr.append(j)
                    return rtnArr

        return rtnArr