class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # set up a double ended queue
        stack = collections.deque()
        # pop the number larger number from the most significant digit
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        # remove the zeros from left
        while stack and stack[0] == '0':
            stack.popleft()
        # remove all k digits from the right
        while stack and k:
            stack.pop()
            k -= 1
        # return the stack that is converted to string
        return "".join(stack) if stack else "0"