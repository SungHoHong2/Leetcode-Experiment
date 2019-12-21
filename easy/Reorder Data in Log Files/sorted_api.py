class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def f(log):
            id_, rest = log.split(" ", 1)

            # The isalpha() methods returns “True” if all characters in the string are alphabet
            # Lexicographic order is the way of ordering of words based on the alphabetical order of their component letters.

            if rest[0].isalpha():
                # print (0, rest, id_)
                return (0, rest, id_)
            else:
                # print(1,)
                return (1,)

        return sorted(logs, key=f)



