# declare a treenode
class TreeNode:
    def __init__(self, start, end, middle):
        # set starting point
        self.start = start
        # set ending point
        self.end = end
        # get the middle point
        self.middle = middle
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
                self.root = TreeNode(start, end, (start + end) // 2)
            # if there is a root
            else:
                # append the node to the TreeNode
                self.add(self.root, start, end)
        # return the result of the TreeNode
        return self.query(self.root)
    def add(self, node, start, end):
        # if the new end is smaller than current middle
        if end < node.middle:
            # if there is left child
            if node.left:
                # append the node to the left child
                self.add(node.left, start, end)
            # if there is not left child
            else:
                # create new left child
                node.left = TreeNode(start, end, (start + end) // 2)
        # if the start pointer is bigger than the middle
        elif start > node.middle:
            # if there is a right child
            if node.right:
                self.add(node.right, start, end)
            # if there is no right child
            else:
                # create a new right child
                node.right = TreeNode(start, end, (start + end) // 2)
        # the new start or end overlaps the current middle
        else:
            # update the start time
            node.start = min(node.start, start)
            # update the end time
            node.end = max(node.end, end)
    def query(self, node):
        # the node is empty
        if not node:
            # return the empty result
            return []
        # merge-sort divide and conquer
        left_intervals = self.query(node.left)
        right_intervals = self.query(node.right)
        # set the return variable
        res = []
        # set the inserted flag
        inserted = False
        # iterate the left intervals
        for lres in left_intervals:
            # if the left intervals overlap with the current node
            if lres[1] >= node.start:
                # create a new overlap node
                res.append([min(lres[0], node.start), node.end])
                # set the inserted flag as true
                inserted = True
                # break from the iteration
                break
            # if the left intervals do not overlap with the current node
            else:
                # append the interval to the result
                res.append(lres)
        # if the inserted flag is false
        if not inserted:
            # append the head interval
            res.append([node.start, node.end])
        # iterate the right intervals
        for rres in right_intervals:
            # if the right interval overlaps with the current interval
            if rres[0] <= node.end:
                # update the interval from the result array
                res[-1][1] = max(node.end, rres[1])
            # if the right interval does not overlap with the current interval
            else:
                # append the interval to the result
                res.append(rres)
        # return the result array
        return res
