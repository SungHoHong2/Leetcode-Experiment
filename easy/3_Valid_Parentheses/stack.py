class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:

            # print(stack, char)
            if char in mapping:

                top_element = ''

                # if stack is true then run top_element = stack.pop()
                # if stack is not true then add top_element = '#'
                top_element = stack.pop() if stack else '#'

                if mapping[char] != top_element:
                    return False

            else:
                stack.append(char)

        return not stack

