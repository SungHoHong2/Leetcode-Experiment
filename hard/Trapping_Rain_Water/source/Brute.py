class Solution:
    def trap(self, height: List[int]) -> int:
        # initialize the answer variable
        ans = 0
        # iterate the list
        for i in range(len(height)):
            # set up the flags for checking maximum left and right
            leftMax = 0
            rightMax = 0
            # find the biggest height of the leftside of the list
            curr = i
            while 0 < curr:
                curr -= 1
                leftMax = max(leftMax, height[curr])
            # find the biggest height of the right of the list
            curr = i
            while curr < len(height)-1:
                curr += 1
                rightMax = max(rightMax, height[curr])
            # calculate the current area that can trap the water
            area = max(min(leftMax, rightMax) - height[i],0)
            # accumulate the answer
            ans += area
        # return the answer
        return ans