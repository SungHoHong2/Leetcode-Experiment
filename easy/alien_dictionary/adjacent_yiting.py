class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dic = {c:i for i,c in enumerate(order)}
        for i in xrange(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            for j in range(min(len(w1),len(w2))):
                if w1[j] != w2[j]:
                    if dic[w1[j]] > dic[w2[j]]:
                        return False
                    break
                else:
                    if len(w1) > len(w2):
                        return False
        return True