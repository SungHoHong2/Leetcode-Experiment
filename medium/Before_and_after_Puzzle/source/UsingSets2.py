class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        # create the map that stores the first string of the phrases as the key
        first = collections.defaultdict(set)
        # create the map that stores the last string of the phrases as the key
        last = collections.defaultdict(set)
        # create the return set
        res = set()
        # iterate the phrases
        for p in phrases:
            # split the phrase into an array of string by space
            strs = p.split(' ')
            # combine the phrases that matches with the set of the last string
            for item in [a+p for a in last[strs[0]]]:
                res.add(item)
            # combine the phrases that matches with the set of the first string
            for item in [p+b for b in first[strs[-1]]]:
                res.add(item)
            # store the first string as the key and add the rest to the set
            first[strs[0]].add(p[len(strs[0]):])
            # store the last string as the key and add the rest to the set
            last[strs[-1]].add(p[:len(p)-len(strs[-1])])
        # return with the sorted result
        return sorted(list(res))