class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:

        first = collections.defaultdict(set)
        last = collections.defaultdict(set)
        res = set()

        # x = {"a", "b", "c"}
        # y = {"c", "e", "f"}
        # x |= y
        # x = {'a', 'b', 'c', 'e', 'f'}

        for p in phrases:
            strs = p.split(' ')

            # if the the match is found in the first string
            if strs[0] in last:
                # combine the value from the (last) with the phrase
                res |= {a + p for a in last[strs[0]]}

            # if the match is found in the last string
            if strs[-1] in first:
                # combine the value from the first
                res |= {p + b for b in first[strs[-1]]}

            # append the [first set] with the phrase that excludes the first string
            first[strs[0]].add(p[len(strs[0]):])

            # append the [last set] with the phrase that excludes the last string
            last[strs[-1]].add(p[:len(p) - len(strs[-1])])

        # return with the sorted result
        return sorted(list(res))