class Solution:
    def trap(self, height: List[int]) -> int:
        """
        y-axis         #
                   #   ## #
                 # ## ######
                    x-axis
        """
        # initialize the answer variable
        ans = 0
        # iterate the list
        for x in range(len(height)):
            # set up the flags for checking maximum left and right
            left_max, right_max = 0, 0
            # find the biggest height of the leftside of the list
            left = x
            while 0 < left:
                left -= 1
                left_max = max(left_max, height[left])
            # find the biggest height of the right of the list
            right = x
            while right < len(height) - 1:
                right += 1
                right_max = max(right_max, height[right])
                # calculate the current area that can trap the water
            area = max(min(left_max, right_max) - height[x], 0)
            # accumulate the answer
            ans += area
        # return the answer
        return ans