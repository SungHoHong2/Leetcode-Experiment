class Solution:

    def firstUniqChar(self, s: str) -> int:

        counter = collections.Counter()

        for item in s:
            counter[item] += 1

        for index, item in enumerate(s):
            if counter[item] == 1:
                return index

        return -1