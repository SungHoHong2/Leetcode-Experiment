class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # define custom sorting
        def f(log):
            # split log into id and the log
            id_, rest = log.split(" ", 1)
            # if the log contains string
            if rest[0].isalpha():
                # give higher priority based on 1) string, 2) lexographical order of the log, order of the id
                return (0, rest, id_)
            # if the log contains digit
            else:
                # give less priority
                return (1,)
        # run the sorted function with the custom sorting
        return sorted(logs, key=f)