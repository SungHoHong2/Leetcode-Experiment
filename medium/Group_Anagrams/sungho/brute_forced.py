class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return []

        rtnTable = {}
        ans = []
        for s in strs:
            tmp = [c for c in s]
            tmp.sort()
            key = "".join(tmp)
            if key not in rtnTable:
                rtnTable[key] = []
                rtnTable[key].append(s)
            else:
                rtnTable[key].append(s)

        rtnResult = []
        for key in rtnTable:
            rtnResult.append(rtnTable[key])

        return rtnResult
