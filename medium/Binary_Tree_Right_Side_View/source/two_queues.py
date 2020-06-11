class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        # include the first-level of the tree to the next_level array
        next_level = deque([root, ])

        # return value
        rightside = []

        while next_level:

            # prepare for the next level
            curr_level = next_level
            next_level = deque()

            # empty the curr_level array
            while curr_level:

                # start the elements from the left
                node = curr_level.popleft()

                # add the child nodes for the next_level array
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # The last element of the curr_level array is the rightmost one.
            rightside.append(node.val)

        return rightside