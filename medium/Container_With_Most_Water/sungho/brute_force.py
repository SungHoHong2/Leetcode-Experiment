class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                maxarea = max(maxarea, min(height[i], height[j]) * (j - i));

        return maxarea