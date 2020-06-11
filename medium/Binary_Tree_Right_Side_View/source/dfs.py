class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        rightside = []

        def helper(node: TreeNode, level: int) -> None:

            # do not add more right node when it exceeds the intended level
            if level == len(rightside):
                rightside.append(node.val)

            # traverse the right node as the priority
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)

        helper(root, 0)
        return rightside