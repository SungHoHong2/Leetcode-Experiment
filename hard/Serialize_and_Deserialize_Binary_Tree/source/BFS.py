class Codec:

    def serialize(self, root):
        # return empty string if the input is invalid
        if not root:
            return ''
        # set the double-ended queue
        queue = collections.deque()
        # append the root to the queue
        queue.append(root)
        # set the return string
        res = ''
        # loop the queue until it is depleted
        while queue:
            # pop item from the left side of the queue
            node = queue.popleft()
            # append 'None,' to the return string and continue if the node is None
            if not node:
                res += 'None,'
                continue
            # append the node value to the return string
            res += str(node.val) + ','
            # append the left child to the queue
            queue.append(node.left)
            # append the right child to the queue
            queue.append(node.right)
        # return the string
        return res

    def deserialize(self, data):
        # return None if the data is invalid
        if not data:
            return None
        # convert the string to an array with ','
        array = data.split(',')
        # create the root node
        root = TreeNode(int(array[0]))
        # create the double-ended queue
        queue = collections.deque()
        # append the root to the queue
        queue.append(root)
        # set the index for the input array
        i = 1
        # loop until the queue or input array is depleted
        while queue and i < len(array):
            # pop the queue from the left
            node = queue.popleft()
            # create the left child node if the item of the array is valid
            if array[i] != 'None':
                node.left = TreeNode(int(array[i]))
                queue.append(node.left)
            i += 1
            # create the right child node if the item of the array is valid
            if array[i] != 'None':
                node.right = TreeNode(int(array[i]))
                queue.append(node.right)
            i += 1
        # return the head of the tree
        return root