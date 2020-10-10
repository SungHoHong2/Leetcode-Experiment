class Solution:
    def maxArea(self, height: List[int]) -> int:
        # set the variable the check the maximum area
        maxarea = 0
        # set the pointer of the left
        l = 0
        # set the pointer of the right
        r = len(height) -1
        # iterate until the items from the list are checked
        while l < r:
            # get the shortest height from the left and right
            _height = min(height[l], height[r])
            # update the maximum area of the height
            maxarea = max(maxarea, _height * (r-l))
            # if the left side is shorter
            if height[l] < height[r]:
                # move from the left
                l += 1
            # if the right side is shorter
            else:
                # move from the right
                r -=1
        # return the maximum area
        return maxarea