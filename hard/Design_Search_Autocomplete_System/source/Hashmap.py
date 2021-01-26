class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        # set a global hashmap[sentence]=times
        self.hashmap = collections.defaultdict(int)
        # set a global prefix
        self.curr = ""
        # store the history in the hashmap
        for i in range(len(sentences)):
            self.hashmap[sentences[i]] = times[i]

    def input(self, c: str) -> List[str]:
        # if search ended
        if c == '#':
            # store the new history to the hashmap
            self.hashmap[self.curr] += 1
            # reset the prefix
            self.curr = ""
        # if ongoing search
        else:
            # accumulate the characters
            self.curr += c
            # create a return list
            ans = list()
            # iterate the hashmap
            for sentence, time in self.hashmap.items():
                # if the accumulated characters are the subset and starts at the beginning of the keys
                if self.curr in sentence and self.curr == sentence[:len(self.curr)]:
                    # append to the return list
                    ans.append((sentence, time))
            # sort the return list by frequency and ascii order
            ans.sort(key=lambda s: (-s[1], s[0]))
            # return three recommendations
            return [t[0] for t in ans][:3]