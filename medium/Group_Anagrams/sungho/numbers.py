class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return []

        rtnTable = {}
        ans = []
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

                # print(count)
            key = tuple(count)
            if key not in rtnTable:
                rtnTable[key] = []
                rtnTable[key].append(s)
            else:
                rtnTable[key].append(s)

        # print(rtnTable)
        rtnResult = []
        for key in rtnTable:
            rtnResult.append(rtnTable[key])

        return rtnResult
