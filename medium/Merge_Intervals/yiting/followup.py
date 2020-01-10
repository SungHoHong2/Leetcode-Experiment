class Node(object):
    def __init__(self, start, end, mid):
        self.start = start
        self.end = end
        self.mid = mid
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.root = None

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        for start, end in intervals:
            if not self.root:
                self.root = Node(start, end, (start + end) / 2)
            else:
                self.add(self.root, start, end)

        return self.query(self.root)

    def add(self, node, start, end):
        if end < node.mid:
            if node.left:
                self.add(node.left, start, end)
            else:
                node.left = Node(start, end, (start + end) / 2)
        elif start > node.mid:
            if node.right:
                self.add(node.right, start, end)
            else:
                node.right = Node(start, end, (start + end) / 2)
        else:
            node.start = min(node.start, start)
            node.end = max(node.end, end)

    def query(self, node):
        if not node:
            return []
        l = self.query(node.left)
        r = self.query(node.right)
        result = []
        insert = False
        for item in l:
            if item[-1] < node.start:
                result.append(item)
            else:
                result.append([min(item[0], node.start), node.end])
                insert = True
                break
        if not insert:
            result.append([node.start, node.end])

        for item in r:
            if item[0] > node.end:
                result.append(item)
            else:
                result[-1][-1] = max(item[-1], node.end)
        return result



