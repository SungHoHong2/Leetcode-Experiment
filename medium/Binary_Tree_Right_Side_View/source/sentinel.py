class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        # add the first level with the sentinel
        queue = deque([root, None, ])

        # return value
        rightside = []

        # set the root node to curr
        curr = root

        # pop the nodes of the each level from the left
        while queue:

            # assign the previous node and the next node
            prev, curr = curr, queue.popleft()

            # add child nodes in the current level to the queue
            while curr:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                # stop until the curr becomes None
                prev, curr = curr, queue.popleft()

            # the current level is finished
            # and prev is its rightmost element
            rightside.append(prev.val)

            # add a sentinel to mark the end
            # of the next level
            if queue:
                queue.append(None)

        return rightside