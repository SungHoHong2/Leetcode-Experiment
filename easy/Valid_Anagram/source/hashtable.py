class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mapper = defaultdict(int)

        for i in s:
            mapper[i] += 1

        for i in t:
            if i not in mapper:
                return False
            else:
                mapper[i] -= 1

        for key, val in mapper.items():
            if val != 0:
                return False

        return True
