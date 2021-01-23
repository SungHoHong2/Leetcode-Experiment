class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        # return true if all the patterns and the inputs are explored
        if not pattern:
            return not text
        # get the result of the validity of the first input
        match = bool(text) and pattern[0] in {text[0], '.'}
        # if the next pattern is '*'(zero or more repeated)
        if len(pattern) >= 2 and pattern[1] == '*':
            # move to next pattern or check if the next input is repeated
            return (self.isMatch(text, pattern[2:]) or match and self.isMatch(text[1:], pattern))
        # if the next pattern is not a repeat
        else:
            # check the first input is valid and move to next input and next pattern
            return match and self.isMatch(text[1:], pattern[1:])
