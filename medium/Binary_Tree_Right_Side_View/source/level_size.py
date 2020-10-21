class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # set the return value
        rightside = []
        # return the empty list if there is no input
        if root is None:
            return rightside
        # create the first level
        queue = deque([root, ])
        # explore the levels in the tree
        while queue:
            # get the length of the current level
            level_length = len(queue)
            # explore the nodes in the current level
            for i in range(level_length):
                # pop the node of the level from the left
                node = queue.popleft()
                # append to the return list if the current node is the rightmost element
                if i == level_length - 1:
                    rightside.append(node.val)
                # add child nodes in the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        # return the list of nodes from the rightside
        return rightside