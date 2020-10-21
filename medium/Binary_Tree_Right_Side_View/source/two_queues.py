class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # set the list that keep record of the right side element
        rightside = []
        # return empty list if there is no input
        if root is None:
            return rightside
        # create the FIFO queue for each level
        next_level = deque([root, ])
        # explore the tree to the last level
        while next_level:
            # get the current level
            curr_level = next_level
            # create a new FIFO queue for the next level
            next_level = deque()
            # explore the nodes in the current level
            while curr_level:
                # pop out the nodes from the left
                node = curr_level.popleft()
                # add the child nodes for the next_level array
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            # the rightmost node in each level is the rightside of the tree
            rightside.append(node.val)
        # return the list of nodes that are from the rightside
        return rightside