class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # set the return value
        rightside = list()
        # return the empty list if there is no input
        if not root:
            return rightside
        # create the first level with the sentinel
        queue = deque([root, None])
        # set a variable to track the rightmost nodes
        prev = None
        # explore the nodes in each level
        while queue:
            # assign the previous node and the next node
            curr = queue.popleft()
            # add child nodes for the next level
            while curr:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                # stop until the current node reaches "None" (end of the level)
                prev, curr = curr, queue.popleft()
            # append the rightmost node to the return list
            rightside.append(prev.val)
            # add a sentinel if there is a next level or let the queue be empty
            if queue:
                queue.append(None)
        # return the list of the rightside nodes
        return rightside
