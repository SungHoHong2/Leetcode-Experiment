
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        # set a global hashmap[sentence]=times
        self.hashmap = collections.defaultdict(int)
        # set a global prefix
        self.curSent = ""
        # store the history in the hashmap
        for i in range(len(sentences)):
            self.hashmap[sentences[i]] = times[i]

    def input(self, c: str) -> List[str]:
        # if the search ended
        if c == '#':
            # store the new history to the hashamp
            self.hashmap[self.curSent] += 1
            # reset the prefix
            self.curSent = ""
        # if ongoing search
        else:
            # accumulate the characters
            self.curSent += c
            # create a return list
            tmp = list()
            # iterate the hashmap
            for sentence, time in self.hashmap.items():
                # if the accumulated characters are the subset and starts at the beginning of the keys
                if self.curSent in sentence and sentence.index(self.curSent) == 0:
                    # append to the return list
                    tmp.append((sentence, time))
            # sort the return list by frequency and ascii order
            tmp.sort(key=lambda s: (-(s[1]), s[0]))
            # return three recommendations
            return [t[0] for t in tmp][:3]