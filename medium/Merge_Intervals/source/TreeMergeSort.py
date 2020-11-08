# declare a treenode
class TreeNode:
    def __init__(self, start, end):
        # set starting point
        self.start = start
        # set ending point
        self.end = end
        # get the middle point
        self.middle = (start + end) // 2
        # set the pointers for the child nodes
        self.left = self.right = None
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # set root node
        self.root = None
        # if there is no intervals
        if not intervals:
            return []
        # iterate the intervals
        for start, end in intervals:
            # if there is no root
            if not self.root:
                # create a root node for the TreeNode
                self.root = TreeNode(start, end)
            # if there is a root
            else:
                # append the node to the TreeNode
                self.add(self.root, TreeNode(start, end))
        # return the result of the TreeNode
        return self.query(self.root)
    def add(self, node, new):
        # if the new end is smaller than current middle
        if new.end < node.middle:
            # if there is left child
            if node.left:
                # append the node to the left child
                self.add(node.left, new)
            # if there is not left child
            else:
                # create new left child
                node.left = new
        # if the start pointer is bigger than the middle
        elif new.start > node.middle:
            # if there is a right child
            if node.right:
                self.add(node.right, new)
            # if there is no right child
            else:
                # create a new right child
                node.right = new
        # the new start or end overlaps the current middle
        else:
            # update the start time
            node.start = min(node.start, new.start)
            # update the end time
            node.end = max(node.end, new.end)
    def query(self, node):
        # the node is empty
        if not node:
            # return the empty result
            return []
        # get the array from the left and the right child
        left_intervals = self.query(node.left)
        right_intervals = self.query(node.right)
        # set the return variable
        res = []
        # set the flag to check whether the current node is merged with the intervals from the left
        inserted = False
        # iterate the left intervals
        for lres in left_intervals:
            # if the left intervals do not overlap with the current node
            if lres[1] < node.start:
                # append the interval to the return array
                res.append(lres)
            # if the left intervals overlap with the current node
            else:
                # merge the interval with the current node and append to the return array
                res.append([min(lres[0], node.start), node.end])
                # break from the iteration and skip adding the current node
                inserted = True
                break
        # if there was no merge of the current node
        if not inserted:
            # append the interval to the return array
            res.append([node.start, node.end])
        # iterate the right intervals
        for rres in right_intervals:
            # if the right interval does not overlap with the current interval
            if node.end < rres[0]:
                # append the interval to the return array
                res.append(rres)
            # if the right interval overlaps with the current interval
            else:
                # merge the interval with the rightmost interval in the return array
                res[-1][1] = max(node.end, rres[1])
        # return the result array
        return res