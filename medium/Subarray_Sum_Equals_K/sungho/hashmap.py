class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {}
        count, sum = 0, 0
        hmap[0] = 1
        for i in nums:
            sum += i

            if ((sum - k) in hmap):
                count += hmap[sum - k]

            if (sum in hmap):
                hmap[sum] += 1
            else:
                hmap[sum] = 1

        return count


