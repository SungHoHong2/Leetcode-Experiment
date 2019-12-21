class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        def sorter(logs):
            id, rest = logs.split(" ", 1)
            if rest[0].isalpha():
                return (0, rest, id)
            else:
                return (1,)

        return sorted(logs, key=sorter)