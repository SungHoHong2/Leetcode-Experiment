class Solution(object):

    # function for generating the next number
    def getNext(self, n):
        # set up the return value
        s = 0
        while n > 0:
            # get the remainder
            dig = n % 10
            # update the n with the quotient
            n = n // 10
            # add the results of the remainder
            s += pow(dig, 2)
        # return the added results
        return s

    def isHappy(self, n):

        # create a hash set
        hashset = set()
        # if n is not 1 and n is not in the hashset
        while n != 1 and n not in hashset:
            # add a number in hashset
            hashset.add(n)
            # generate the next number
            n = self.getNext(n)

        return n == 1