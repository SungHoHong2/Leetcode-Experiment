class Solution:

    def backtrack(self, combination, next_digits):
        # if recursive tree has reached its leaf
        if len(next_digits) == 0:
            # append the finished combination to the return list
            self.output.append(combination)
        # if there are still digits to check
        else:
            # iterate the letters which are mapped to the number
            for letter in self.phone[next_digits[0]]:
                # provide the combination and the next digit to the next recursive tree
                self.backtrack(combination + letter, next_digits[1:])

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # set the map for all the characters mapped to the number
        self.phone = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']}
        # set the return list
        self.output = []
        # if there is no input
        if not digits:
            # return the empty list
            return self.output
            # invoke the recursive function
        self.backtrack("", digits)
        return self.output