class Solution:

    def recursion(self, combination, next_digits):
        # set a return array that stores all the combinations
        ans = list()
        # return the combination to the return list if the input is depleted
        if not next_digits:
            return [combination]
        # iterate the letters which are mapped to the number
        for c in self.phone[next_digits[0]]:
            # extend the combinations to the return array
            ans += self.recursion(combination + c, next_digits[1:])
        # return the combinations
        return ans

    def letterCombinations(self, digits: str) -> List[str]:
        # return an empty list if there is no input
        if not digits:
            return list()
        # create a dictionary that maps all the letters with the numbers
        self.phone = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']}
        # return the combination from the recursion
        return self.recursion("", digits)