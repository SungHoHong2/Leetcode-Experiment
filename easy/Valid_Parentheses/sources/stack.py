class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        # iterate the string
        for c in s:
            # if the char is part of the mapping
            if c in mapping:

                # if the stack is not empty
                if stack:
                    # pop the item
                    top = stack.pop()

                # if the stack is empty
                else:
                    top = "#"

                # if the popped item does not equal with the mapping
                if mapping[c] != top:
                    # return false
                    return False

            # if char is not part of the mapping
            else:
                # append the char in the stack
                stack.append(c)

        # if the stack is empty return True
        return not stack