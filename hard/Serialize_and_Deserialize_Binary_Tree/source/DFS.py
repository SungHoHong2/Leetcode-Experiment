class Codec:
    def serialize(self, root):
        def dfs(node, string):
            # append the string with "None," when the node is blank
            if not node:
                return string + 'None,'
            # append the value to the return string
            string += str(node.val) + ','
            # append the value from the left child
            string = dfs(node.left, string)
            # append the value from the right child
            string = dfs(node.right, string)
            # return the string
            return string
        # start dfs
        return dfs(root, "")

    def deserialize(self, data):
        def dfs(queue):
            # if the current item is None
            if queue[0] == 'None':
                # pop the current item
                queue.popleft()
                # return None
                return None
            # create the node with the current item
            root = TreeNode(queue.popleft())
            # create the left child
            root.left = dfs(queue)
            # create the right child
            root.right = dfs(queue)
            # return the node
            return root
        # return the reconstructed tree from deserialization
        return dfs(collections.deque(data.split(',')))