class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        res = 0

        stack = [float('inf')]

        # traverse through the elements of array
        for a in A:

            # if last element in the stack is smaller than the element
            while stack[-1] <= a:
                print(stack, a)
                mid = stack.pop()
                res += mid * min(stack[-1], a)
                print('first', res, mid, min(stack[-1], a))

            # append the element
            stack.append(a)

        while len(stack) > 2:
            res += stack.pop() * stack[-1]
            print('second', res)

        return res