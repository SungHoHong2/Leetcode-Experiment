class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:

        # create the map that stores the first string of the phrases as the key and the rest as a set
        first = collections.defaultdict(set)
        # create the map that stores the last string of the phrases as the key and the rest as a set
        last = collections.defaultdict(set)
        # create the return set
        res = set()

        # x = {"a", "b", "c"}
        # y = {"c", "e", "f"}
        # x |= y
        # x = {'a', 'b', 'c', 'e', 'f'}

        # iterate the phrases
        for p in phrases:
            # split the phrase into an array of string by space
            strs = p.split(' ')
            # if the first string of the current phrase matches with some last string of the other phrase
            if strs[0] in last:
                # combine the overlapping phrases {rest of the last string + last string}
                print(strs[0], last[strs[0]], p)
                res |= {a + p for a in last[strs[0]]}
            # if the last string of the current phrase matches with the first string of the other phrase
            if strs[-1] in first:
                # combine the overlapping phrases {first string + rest of the first string}
                res |= {p + b for b in first[strs[-1]]}
            # store the first string as the key and the rest in a set
            first[strs[0]].add(p[len(strs[0]):])
            # store the last string as the key and the rest in a set
            last[strs[-1]].add(p[:len(p) - len(strs[-1])])
        # return with the sorted result
        return sorted(list(res))