
class Solution:
    def trap(self, height: List[int]) -> int:
        # set the answer
        ans = 0
        # set the stack
        stack = list()
        # iterate the heights
        for current in range(len(height)):
            # loop the stack until the heights lower than the current height is empty
            while stack and (height[current] > height[stack[-1]]):
                # pop the previous heights that are smaller than the current height
                top = stack.pop()
                # finish the loop if there is no more previous heights
                if not stack:
                    break
                    # calculate the distance
                x = current - stack[-1] - 1
                # calculate the avialble height height
                y = min(height[current], height[stack[-1]]) - height[top]
                # aggregate the available space for the rain
                ans += x * y
                # print(stack, {'left': height[stack[-1]], 'mid' : height[top],  'right' : height[current], 'area': x*y})
            # append the previous heights in the stack
            stack.append(current)
        return ans