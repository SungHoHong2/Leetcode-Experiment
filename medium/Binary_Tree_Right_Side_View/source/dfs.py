class Solution:
    def helper(self, node, level):
        # current level matches with the number of returning nodes
        if level == len(self.rightside):
            # append the node to the return list
            self.rightside.append(node.val)
        # explore the right node as the priority
        for child in [node.right, node.left]:
            if child:
                self.helper(child, level + 1)

    def rightSideView(self, root: TreeNode) -> List[int]:
        # set the return value
        self.rightside = []
        # return the empty list if there is no input
        if root is None:
            return self.rightside
        # invoke the dfs recursion
        self.helper(root, 0)
        # return the list of the nodes from the rightside
        return self.rightside