class Solution(object):

    # function for finding the next number
    def getNext(self, n):
        s = 0
        while n > 0:
            dig = n % 10
            n = n // 10
            s += dig ** 2
        return s

    def isHappy(self, n):
        # set up the slow number
        slow = n
        # set up the fast number that goes one step ahead of the slow number
        fast = self.getNext(n)
        # loop until fast reach 1 or slow and fast meets a cycle
        while fast != 1 and slow != fast:
            # slow moves one step at a time
            slow = self.getNext(slow)
            # fast moves two steps at a time
            fast = self.getNext(self.getNext(fast))
        # return if fast returns 1
        return fast == 1