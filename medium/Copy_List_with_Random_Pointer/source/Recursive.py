class Solution:
    def __init__(self):
        # initialize a cache
        self.visited = dict()
    def copyRandomList(self, head: 'Node') -> 'Node':
        # return none if the node is null
        if not head:
            return none
        # return the cached node if the node is in the cache
        if head in self.visited:
            return self.visited[head]
        # create a node
        node = Node(head.val, None, None)
        # add the node to the cache
        self.visited[head] = node
        # receive the recursive function from the next
        node.next = self.copyRandomList(head.next)
        # receive the recursive function from the random
        node.random = self.copyRandomList(head.random)
        # return the node
        return node