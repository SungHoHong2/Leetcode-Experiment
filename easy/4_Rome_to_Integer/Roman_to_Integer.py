class Solution:
    def romanToInt(self, s: str) -> int:

        romanDic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        # print(romanDic)

        rtnValue = 0
        subtract = False

        for i in range(0, len(s) - 1):
            if romanDic[s[i]] == romanDic[s[i + 1]] or romanDic[s[i]] > romanDic[s[i + 1]]:
                subtract = False
            elif romanDic[s[i]] < romanDic[s[i + 1]]:
                subtract = True

            if subtract == False:
                print("add", s[i])
                rtnValue += romanDic[s[i]]
            elif subtract == True:
                print("subtract", s[i])
                rtnValue -= romanDic[s[i]]

        rtnValue += romanDic[s[len(s) - 1]]

        return rtnValue