class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        # set a global one-level hashmap[sentence[0]] = hashmap[sentence[:]] = int
        self.hashmap = collections.defaultdict(dict)
        # set a global prefix
        self.curr = ""
        # store the history in the hashmap
        for i in range(len(sentences)):
            self.hashmap[sentences[i][0]][sentences[i]] = times[i]

    def input(self, c: str) -> List[str]:
        # if the search ended
        if c == '#':
            # store the new sentence to the hashmap
            if self.curr not in self.hashmap[self.curr[0]]:
                self.hashmap[self.curr[0]][self.curr] = 0
            # update the frequency of the sentence
            self.hashmap[self.curr[0]][self.curr] += 1
            # reset the global prefix
            self.curr = ""
            # if ongoing search
        else:
            # accumulate the characters
            self.curr += c
            # create a return list
            ans = list()
            # iterate the hashmap
            for sentence in self.hashmap[self.curr[0]]:
                # if the accumulated characters are the subset and starts at the beginning of the keys
                if self.curr in sentence and self.curr == sentence[:len(self.curr)]:
                    # append to the return list
                    ans.append((sentence, self.hashmap[self.curr[0]][sentence]))
            # sort the return list by frequency and ascii order
            ans.sort(key=lambda s: (-s[1], s[0]))
            # return three recommendations
            return [t[0] for t in ans][:3]