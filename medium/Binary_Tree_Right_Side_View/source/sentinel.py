class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # set the return value
        rightside = []
        # return the empty list if there is no input
        if root is None:
            return rightside
        # create the first level with the sentinel
        queue = deque([root, None, ])
        # set the pointer to the root node
        curr = root
        # explore the nodes in each level
        while queue:
            # assign the previous node and the next node
            prev = curr
            curr = queue.popleft()
            # add child nodes for the next level
            while curr:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                # stop until the node the queue reaches "None" (end of the level)
                prev, curr = curr, queue.popleft()
            # append the rightmost node to the return list
            rightside.append(prev.val)
            # add a sentinel to mark the end of the new level
            if queue:
                queue.append(None)
        # return the list of the rightside nodes
        return rightside