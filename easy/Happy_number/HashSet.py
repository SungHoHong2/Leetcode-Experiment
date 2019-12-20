class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def getNext(n):
            s = 0
            while n > 0:
                n, dig = divmod(n, 10)
                s += dig ** 2
            return s

        hashset = set()
        while n != 1 and n not in hashset:
            hashset.add(n)
            n = getNext(n)

        return n == 1