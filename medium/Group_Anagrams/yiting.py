class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        test = {}
        result = []
        for i in range(len(strs)):
            tmp = sorted(strs[i])
            tmp1 = "".join(tmp)

            if tmp1 in test:
                result[test[tmp1]].append(strs[i])
            else:
                n = len(test)

                test[tmp1] = n
                result.append([strs[i]])

        return result





