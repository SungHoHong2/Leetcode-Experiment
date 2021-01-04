class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # return None if the node is Null
        if not head:
            return None
        # set the current pointer to the head
        ptr = head
        # loop until the Linked-list is depleted
        while ptr:
            # create a new node
            new_node = Node(ptr.val, None, None)
            # interweave the new node
            new_node.next, ptr.next = ptr.next, new_node
            # move the current pointer forward
            ptr = ptr.next.next
        # set the current pointer to the head
        ptr = head
        # loop until the Linked-list is depleted
        while ptr:
            # if the node has a random pointer
            if ptr.random:
                # add the random pointer to the new node
                ptr.next.random = ptr.random.next
            # if there is no random pointer
            else:
                # mark the random pointer to None
                ptr.next.random = None
            # connect the new node with the new node
            ptr = ptr.next.next
        # set the current pointer
        ptr_new = head.next
        # loop until the new Linked-list is depleted
        while ptr_new:
            # connect the only nodes from the new linked-list
            ptr_new.next = ptr_new.next.next if ptr_new.next else None
            ptr_new = ptr_new.next
        # return the new Linked-list
        return head.next