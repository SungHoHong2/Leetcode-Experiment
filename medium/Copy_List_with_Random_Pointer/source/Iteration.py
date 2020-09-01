class Solution(object):
    def __init__(self):
        # create a cache
        self.visited = {}
    # get cloned node function
    def getClonedNode(self, node):
        # if the node is NULL
        if not node:
            # return None
            return None
        # if the node is in the cache
        if node in self.visited:
            # return the node from the cache
            return self.visited[node]
        # save the node in the cache
        self.visited[node] = Node(node.val, None, None)
        # return the node
        return self.visited[node]
    def copyRandomList(self, head):
        # if hte node is NULL
        if not head:
            # return None
            return None
        # save the header for the original linked-list
        old_node = head
        # create a header for the new linked-list
        new_node = Node(old_node.val, None, None)
        # save the pointer to return the header of the new linked-list
        self.visited[old_node] = new_node
        # loop until the original node is depleted
        while old_node != None:
            # create the node from the random pointer
            new_node.random = self.getClonedNode(old_node.random)
            # create the node from the next pointer
            new_node.next = self.getClonedNode(old_node.next)
            # move the previous linked-list forward
            old_node = old_node.next
            # move the new linked-list forward
            new_node = new_node.next
        # return the header of the new linked-list
        return self.visited[head]