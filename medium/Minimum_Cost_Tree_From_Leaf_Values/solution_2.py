class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        res = 0

        stack = [float('inf')]

        # traverse through the elements of array
        for a in A:
            # just find the next greater element in the array
            # if element is smaller than the current item
            # 8 [2] a(4)
            while stack[-1] <= a:
                # print(stack, a)
                # get the smaller element
                mid = stack.pop()

                # compare the left node and the right node of the middle element
                # mutliply and add as a result
                res += mid * min(stack[-1], a)
                # print('first', res, mid, min(stack[-1], a))

            # first append the elements
            stack.append(a)

        # we assume the left overs are well ordered from big to small
        # 6, 4
        # so we simply multiply from right to left
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
            # print('second', res)

        return res