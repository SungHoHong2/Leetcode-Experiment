class Solution:

    def addToHash(self, lists, m, i, sum):
        # record the sum if the array reaches the second half
        if i == len(lists) // 2:
            m[sum] += 1
        # accumulate if the array is within the first half
        else:
            for a in lists[i]:
                self.addToHash(lists, m, i + 1, sum + a)

    def countComplements(self, lists, m, i, complement):
        # return the counts if the sum matches the complement
        if i == len(lists):
            return m[complement]
        # set the counter to record the answer
        cnt = 0
        # accumulate the second half of the array and count the results that reaches the complement
        for a in lists[i]:
            cnt += self.countComplements(lists, m, i + 1, complement - a)
        # return the total number of counts
        return cnt

    def nSumCount(self, lists):
        # create a table that records the complements
        m = collections.defaultdict(int)
        # sum up the the first half and store them as complements in the hashtable
        self.addToHash(lists, m, 0, 0)
        # check if the sum reaches zero by comparing the complements of the first with the second half
        return self.countComplements(lists, m, len(lists) // 2, 0)

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # introduce an algorithm that allows n arrays
        return self.nSumCount([A, B, C, D])