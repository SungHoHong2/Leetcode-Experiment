class Solution:
    def backtrack(self, combination, next_digits):
        # append the combination to the return list if the input is depleted
        if len(next_digits) == 0:
            self.output.append(combination)
        # if there are still digits to check
        else:
            # iterate the letters which are mapped to the number
            for letter in self.phone[next_digits[0]]:
                # provide the combination and the next digit to the next recursive tree
                self.backtrack(combination + letter, next_digits[1:])

    def letterCombinations(self, digits):
        # set the map for all the characters mapped to the number
        self.phone = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']}
        # set the answer as an array
        self.output = list()
        # return the answer if there is no input
        if not digits:
            return self.output
        # invoke the recursive function
        self.backtrack("", digits)
        # return the list
        return self.output