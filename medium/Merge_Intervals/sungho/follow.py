class TreeNode:
    def __init__(self, start, end, middle):
        self.start = start
        self.end = end
        self.middle = middle
        self.left = self.right = None


class Solution:
    def __init__(self):
        self.root = None

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # if there is no intervals
        if not intervals:
            return []

        for start, end in intervals:

            # if there is no root
            if not self.root:
                # create a root node
                self.root = TreeNode(start, end, (start + end) // 2)

            # if there is a root
            else:
                # add a root node
                self.add(self.root, start, end)

        return self.query(self.root)

    def add(self, node, start, end):

        # comparing with the new with the previous
        # the new one does not overlaps with the previous
        if end < node.middle:
            if node.left:
                self.add(node.left, start, end)
            else:
                # create new node left
                node.left = TreeNode(start, end, (start + end) // 2)

        elif start > node.middle:
            if node.right:
                self.add(node.right, start, end)
            else:
                # create new node right
                node.right = TreeNode(start, end, (start + end) // 2)

        # the new one overlaps with the previous
        else:
            node.start = min(node.start, start)
            node.end = max(node.end, end)

    def query(self, node):
        if not node:
            return []

        # merge-sort divide and conquer
        left_intervals = self.query(node.left)
        right_intervals = self.query(node.right)
        res = []

        inserted = False

        # comparing with the first element of the array with the next array
        #     |  |
        # [[1,6],[8,10],[15,18]]
        for lres in left_intervals:
            if lres[1] >= node.start:
                res.append([min(lres[0], node.start), node.end])
                inserted = True
                break
            else:
                res.append(lres)

        # appending the head
        if not inserted:
            res.append([node.start, node.end])

        # comparing with the last element of the array with the previous array
        #            |   |
        # [[1,6],[8,10],[15,18]]
        for rres in right_intervals:
            if rres[0] <= node.end:
                res[-1][1] = max(node.end, rres[1])
            else:
                res.append(rres)

        return res
