# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def rserialize(root, string):
            # append the string with "None," when the node is blank
            if root is None:
                string += 'None,'
            # if the node has value
            else:
                # append the value to the return string
                string += str(root.val) + ','
                # append the value from the left child
                string = rserialize(root.left, string)
                # append the value from the right child
                string = rserialize(root.right, string)
            # return the string
            return string

        # start dfs
        return rserialize(root, '')

    def deserialize(self, data):
        def rdeserialize(l):
            # if the current item is None
            if l[0] == 'None':
                # pop the current item
                l.pop(0)
                # return None
                return None
            # create the node with the current item
            root = TreeNode(l[0])
            # pop the current item
            l.pop(0)
            # create the left child
            root.left = rdeserialize(l)
            # create the right child
            root.right = rdeserialize(l)
            # return the node
            return root

        # create the array by dividing the string with ','
        data_list = data.split(',')
        # invoke recursion
        root = rdeserialize(data_list)
        # return the tree
        return root
