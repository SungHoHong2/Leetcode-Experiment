class Solution:
    def backtrack(self, combination, next_digits):
        # set a list as the result
        ans = list()
        # if recursive tree has reached its leaf
        if len(next_digits) == 0:
            # append the possible answer as the result
            ans.append(combination)
        # if there are still digits to check
        else:
            # append the results to the return array from the next recursions
            for letter in self.phone[next_digits[0]]:
                ans.extend(self.backtrack(combination + letter, next_digits[1:]))
        # return the result
        return ans

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
        # if there is no input
        if not digits:
            return list()
        # return the list from recursion
        return self.backtrack("", digits)
