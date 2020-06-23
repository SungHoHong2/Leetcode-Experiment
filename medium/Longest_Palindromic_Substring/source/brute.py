class Solution:

    def longestPalindrome(self, s: str) -> str:

        checkLongest = 0
        biggestString = None

        if len(s) == 0:
            return ""

        if len(s) == 1:
            return s

        def checkMatch(index):

            oddLength = 0
            evenLength = 0

            # check the odd palindrome
            left = index - 1
            right = index + 1

            while left >= 0 and right < len(s):

                if s[left] == s[right]:
                    oddLength += 1
                else:
                    break

                left -= 1
                right += 1

            # check the even palindrome
            left = index - 1
            right = index

            while left >= 0 and right < len(s):

                if s[left] == s[right]:
                    evenLength += 1
                else:
                    break

                left -= 1
                right += 1

            if oddLength >= evenLength:
                return index - oddLength, index + oddLength
            elif oddLength < evenLength:
                return index - evenLength, index + evenLength - 1

        for i in range(1, len(s)):
            left, right = checkMatch(i)

            if checkLongest < len(s[left:right + 1]):
                checkLongest = len(s[left:right + 1])
                biggestString = s[left:right + 1]

        return biggestString