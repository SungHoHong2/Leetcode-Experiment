class Solution:
    def trap(self, height: List[int]) -> int:
        # set the pointers for left and right
        left = 0
        right = len(height) - 1
        # store the record for the largest available space for the rain
        ans = 0
        # store the record for the largest left and right
        left_max = right_max = 0
        # loop until left and right converges
        while left < right:
            # if right is higher
            if height[left] < height[right]:
                # record the largest left if left is going up
                if height[left] >= left_max:
                    left_max = height[left]
                # aggregate the available space if the left is going down
                else:
                    ans += (left_max - height[left])
                # move left to right
                left+=1;
            # if the left is higher
            else:
                # record the largest right if right is going up
                if height[right] >= right_max:
                    right_max = height[right]
                # aggregate the available space if the right is going down
                else:
                    ans += (right_max - height[right])
                # move right to left
                right -=1
        # return the accumulated area
        return ans