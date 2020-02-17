class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        interpret_digit = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        if not digits:
            return []

        # init the array
        all_combinations = ['']

        # iterate the digits
        for digit in digits:

            # create temp list
            current_combinations = list()

            # iterate the alphabets of the digit
            for letter in interpret_digit[digit]:

                # iterate all the possible combination
                for combination in all_combinations:
                    # append the letter
                    current_combinations.append(combination + letter)

            # update all the possible combination
            all_combinations = current_combinations

        return all_combinations


