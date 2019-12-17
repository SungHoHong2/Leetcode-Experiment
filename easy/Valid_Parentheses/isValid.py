class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in mapping:
                if stack:
                    top = stack.pop()
                else:
                    top = "#"
                if mapping[c] != top:
                    return False

            else:
                stack.append(c)

        return not stack
