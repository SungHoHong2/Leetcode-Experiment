class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dict = collections.defaultdict(list)
        for pair in points:
            tmp = pair[0] ** 2 + pair[1] ** 2
            dict[tmp].append(pair)

        result = []
        for key in sorted(dict.keys()):

            while dict[key]:
                if len(result) < K:
                    result.append(dict[key].pop())
                else:
                    break

        return result


