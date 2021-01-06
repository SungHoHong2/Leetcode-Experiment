class Solution:
    def maxArea(self, height: List[int]) -> int:
        # set the variable the check the maximum area
        area = 0
        # set the pointer of the left
        left = 0
        # set the pointer of the right
        right = len(height) - 1
        # iterate until the items from the list are checked
        while left < right:
            # get the shortest height from the left and right
            top = min(height[left], height[right])
            # update the maximum area of the height
            area = max(area, top * (right-left))
            # if the left side is shorter
            if height[left] < height[right]:
                # move from the left
                left += 1
            # if the right side is shorter
            else:
                # move from the right
                right -= 1
        # return the maximum area
        return area