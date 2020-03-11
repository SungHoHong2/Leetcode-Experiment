class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        dict = collections.defaultdict(list)
        dict['2'] = ['a', 'b', 'c']
        dict['3'] = ['d', 'e', 'f']
        dict['4'] = ['g', 'h', 'i']
        dict['5'] = ['j', 'k', 'l']
        dict['6'] = ['m', 'n', 'o']
        dict['7'] = ['p', 'q', 'r', 's']
        dict['8'] = ['t', 'u', 'v']
        dict['9'] = ['w', 'x', 'y', 'z']
        result = []

        def backtrack(combine, nextdigits):
            if not nextdigits:
                result.append(combine)
            else:
                for c in dict[nextdigits[0]]:
                    backtrack(combine + c, nextdigits[1:])

        if digits:
            backtrack("", digits)

        return result
