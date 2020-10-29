class Solution:
    def findMedianSortedArrays(self, A, B):
        # get the total length of of array A and B
        l = len(A) + len(B)
        # return the single median if the array is odd
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        # return the median from two values if the array is even
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        # if there is no array A
        if not a:
            return b[k]
        # if there is no array B
        if not b:
            return a[k]

        # get the middle index from both array a and b
        ia, ib = len(a) // 2, len(b) // 2

        # get the median value from both a and b
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:

            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)