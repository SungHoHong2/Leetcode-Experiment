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

        slow = n
        fast = getNext(n)
        while fast != 1 and slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))

        return fast == 1