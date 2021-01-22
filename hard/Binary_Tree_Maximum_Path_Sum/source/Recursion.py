class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def bsearch(node):
            # return 0 if it reached the leaf
            if not node:
                return 0
            # get the maximum score from the left branch
            left_sum = max(bsearch(node.left), 0)
            # get the maximum score from the right branch
            right_sum = max(bsearch(node.right), 0)
            # update the highest score gained from the complete path
            self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)
            # return the largest possible path that starts from the leaf to the current node
            return node.val + max(left_sum, right_sum)
        # set a global variable to keep track of the maximum sum
        self.max_sum = float('-inf')
        # run the recursion
        bsearch(root)
        # return the maximum sum
        return self.max_sum