class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        # traverse the node while comparing the tree between S and T
        return self.traverse(s, t)

    # the function of traversing the node
    def traverse(self, s, t):

        # if traversed all the subsets of S and found no equal to T
        if not s:
            # return false
            return False

        # if S and T are equal
        # if the left subtree of S and T are equal
        # if the right subtree of S and T are equal
        return self.equals(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t)

    # the function that checks whether the tree of x and y are equal
    def equals(self, x, y):

        # if both x and y are NULL
        if not x and not y:
            return True

            # if only one of x and y are NULL
        if not x or not y:
            return False

        # if the parent, left and right child are all equal
        return x.val == y.val and self.equals(x.left, y.left) and self.equals(x.right, y.right)


