# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(node):
            # return 0 if it reached the leaf
            if not node:
                return 0
            # get the maximum sum from the left and right node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            # get the total sum of the path that excludes the parent node
            price_newpath = node.val + left_gain + right_gain
            # discard the parent node path if the total sum is higher
            self.max_sum = max(self.max_sum, price_newpath)
            # returning and building up a path that creates the total sum with the parent node
            return node.val + max(left_gain, right_gain)

        # set a global variable to keep track of the maximum sum
        self.max_sum = float('-inf')
        # run the recursion
        max_gain(root)
        # return the maximum sum
        return self.max_sum