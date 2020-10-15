class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        # set the variable to return the sum of non-leaf nodes
        res = 0
        # append infinite value to the stack
        stack = [float('inf')]
        # iterate the items from the input
        for a in A:
            # loop when the current item is bigger than the latest item
            while stack[-1] <= a:
                # pop the latest item
                latest = stack.pop()
                # get the neighboring items
                new_neighbor = a
                old_neighbor = stack[-1]
                # multiply with the smallest neighbor and accumulate the result
                res += latest * min(new_neighbor, old_neighbor)
            # append the elements according to the descending order
            stack.append(a)
        # since the array is ordered, multiply from right to left
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        # return the accumulated result
        return res