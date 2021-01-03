class TreeNode:
    def __init__(self, start, end):
        # set starting point
        self.start = start
        # set ending point
        self.end = end
        # get the middle point
        self.middle = (start + end) // 2
        # set the pointers for the child nodes
        self.left, self.right = None, None


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # return empty list if there is no intervals
        if not intervals:
            return list()
        # set root node with the first interval
        root = TreeNode(intervals[0][0], intervals[0][1])
        # iterate the intervals
        for interval in intervals[1:]:
            # append the node to the TreeNode
            self.add(root, TreeNode(interval[0], interval[1]))
        # return the result of the TreeNode
        return self.query(root)

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
        elif node.middle < new.start:
            # if there is a right child
            if node.right:
                self.add(node.right, new)
            # if there is no right child
            else:
                node.right = new
        # the new start or end overlaps the current middle
        else:
            # update the start time
            node.start = min(node.start, new.start)
            # update the end time
            node.end = max(node.end, new.end)

    def query(self, node):
        # set the return variable
        ans = list()
        # return the empty result if the node is empty
        if not node:
            return ans
        # get the array from the left and the right child
        lefts, rights = self.query(node.left), self.query(node.right)
        # iterate the left intervals
        for left in lefts:
            # if the left intervals do not overlap with the current node
            if left[1] < node.start:
                # append the interval to the return array
                ans.append(left)
            # if the left intervals overlap with the current node
            else:
                # merge the interval with the current node
                node.start = min(node.start, left[0])
                # break to skip appending the future nodes that overlaps with the current node
                break
        # append the current node to the return array
        ans.append([node.start, node.end])
        # iterate the right intervals
        for right in rights:
            # if the right interval does not overlap with the current interval
            if node.end < right[0]:
                # append the interval to the return array
                ans.append(right)
            # if the right interval overlaps with the current interval
            else:
                # merge the interval with the rightmost interval in the return array
                ans[-1][1] = max(ans[-1][1], right[1])
                # return the result array
        return ans