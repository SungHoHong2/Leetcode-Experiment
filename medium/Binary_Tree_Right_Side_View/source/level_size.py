class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        queue = deque([root, ])
        rightside = []

        while queue:
            # get the length of the level
            level_length = len(queue)

            # iterate through the level
            for i in range(level_length):

                # pop the node of the level from the left
                node = queue.popleft()

                # if it's the rightmost element
                if i == level_length - 1:
                    rightside.append(node.val)

                # add child nodes in the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return rightside