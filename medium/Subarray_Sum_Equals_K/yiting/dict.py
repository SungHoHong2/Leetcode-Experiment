class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = collections.defaultdict(int)
        count[0] = 1
        n = 0
        s = 0
        for item in nums:
            s += item
            n += count[s - k]
            count[s] += 1

        return n