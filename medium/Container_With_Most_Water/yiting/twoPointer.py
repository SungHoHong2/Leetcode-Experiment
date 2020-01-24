class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxs = 0
        l = 0
        r = len(height) - 1

        while l < r:
            left = height[l]
            right = height[r]
            s = min(left, right) * (r - l)
            if s > maxs:
                maxs = s
            if left > right:
                r -= 1
            else:
                l += 1

        return maxs