# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 1

        def depth(node):
            # reached the leaf
            if not node: return 0

            # get the longest depth from the left
            L = depth(node.left)

            # get the longest depth from the right
            R = depth(node.right)

            # keep record of the longest width between the leaves with the longest depth
            self.ans = max(self.ans, L + R + 1)

            # keep record of the leaf with the longest depth
            return max(L, R) + 1

        depth(root)

        # reduce one since the root is counted twice
        return self.ans - 1