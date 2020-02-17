class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        result = []
        n = 0
        if not paths:
            return []
        dict = {}
        for path in paths:
            tmp = path.split(" ")
            n += len(tmp) - 1
            for i in range(1, len(tmp)):
                content = tmp[i].split("(")[1].split(")")[0]

                if content not in dict:
                    dict[content] = []
                dict[content].append(tmp[0] + "/" + tmp[i].split("(")[0])

        for item in dict.values():
            if len(item) > 1:
                result.append(item)

        return result
