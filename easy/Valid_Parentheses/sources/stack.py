class Solution:
    def isValid(self, s: str) -> bool:

        # set up the stack
        stack = []

        # create a hashtable that maps the parenthesis
        mapping = {")": "(", "}": "{", "]": "["}

        # iterate the chars from the string
        for char in s:

            # if the char is the closing part of the parenthesis
            if char in mapping:

                # if stack is true then run top_element = stack.pop()
                # if stack is not true then add top_element = '#'
                top_element = stack.pop() if stack else '#'

                # if the top element is not the opening part of the parenthesis
                if mapping[char] != top_element:
                    return False

            # if the char is not the closing part of the parenthesis
            else:
                # append the stack
                stack.append(char)

        # return true only when the stack is empty
        return not stack

