class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        tsum = [0 for i in range(len(nums) + 1)]
        # print(nums,tsum)

        tsum[0] = 0
        for i in range(1, len(nums) + 1):
            tsum[i] = tsum[i - 1] + nums[i - 1]

        # print(tsum)
        for start in range(len(nums)):
            for end in range(start + 1, len(nums) + 1):
                if tsum[end] - tsum[start] == k:
                    count += 1

        print(count)
        return count

