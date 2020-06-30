class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        # set a tracker for S uisng preordering
        sTracker = []
        self.preorder(s, sTracker)

        # set a tracker of T using preordering
        tTracker = []
        self.preorder(t, tTracker)

        # convert the arrays to string
        sString = ''.join(sTracker)
        tString = ''.join(tTracker)

        # if T is a subset of S
        if tString in sString:
            return True
        else:
            return False

    # preorder function
    def preorder(self, node, tracker):

        # mark the end of the node
        if not node:
            tracker.append('#')
            return

        # append the node with value
        tracker.append(':' + str(node.val))

        # traverse the tree
        self.preorder(node.left, tracker)
        self.preorder(node.right, tracker)
