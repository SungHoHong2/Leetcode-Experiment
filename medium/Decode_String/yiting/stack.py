class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        result = ''
        num = 0
        for c in s:
            if c == '[':
                stack.append(result)
                stack.append(num)
                result = ''
                num = 0
            elif c == ']':
                n = stack.pop()
                pre = stack.pop()
                result = pre + result * n
            elif c.isdigit():
                num = num * 10 + int(c)
            else:
                result += c

        return result
