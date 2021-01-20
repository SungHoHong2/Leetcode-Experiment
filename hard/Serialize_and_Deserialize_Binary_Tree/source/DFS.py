# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        def rserialize(node, string):
            # append the string with "None," when the node is blank
            if not node:
                string += 'None,'
            # if the node has value
            else:
                # append the value to the return string
                string += str(node.val) + ','
                # append the value from the left child
                string = rserialize(node.left, string)
                # append the value from the right child
                string = rserialize(node.right, string)
            # return the string
            return string

        # start dfs
        return rserialize(root, '')

    def deserialize(self, data):
        def rdeserialize(queue):
            # if the current item is None
            if queue[0] == 'None':
                # pop the current item
                queue.popleft()
                # return None
                return None
            # create the node with the current item
            root = TreeNode(queue[0])
            # pop the current item
            queue.popleft()
            # create the left child
            root.left = rdeserialize(queue)
            # create the right child
            root.right = rdeserialize(queue)
            # return the node
            return root

        # invoke recursion using the splitted FIFO queue
        root = rdeserialize(collections.deque(data.split(',')))
        # return the tree
        return root