class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = ''.join(ch for ch in s if ch.isalnum())

        if new == "":
            return True
        new = new.lower()

        p = 0
        n = len(new) - 1
        while n != p and n >= 0 and p < len(new):
            if new[p] != new[n]:
                return False
            p += 1
            n -= 1

        return True
