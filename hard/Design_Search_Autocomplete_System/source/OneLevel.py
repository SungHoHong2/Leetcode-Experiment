class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        # set a global prefix
        self.curSent = ""

        # store the history in the hashmap
        self.arr = collections.defaultdict(dict)
        for i in range(len(sentences)):
            self.arr[ord(sentences[i][0]) - ord('a')][sentences[i]] = times[i]

    def input(self, c: str) -> List[str]:
        # if the search ended
        if c == '#':
            # store the new history to the hashamp
            if self.curSent not in self.arr[ord(self.curSent[0]) - ord('a')]:
                self.arr[ord(self.curSent[0]) - ord('a')][self.curSent] = 0
            self.arr[ord(self.curSent[0]) - ord('a')][self.curSent] += 1
            self.curSent = ""
        # if ongoing search
        else:
            # accumulate the characters
            self.curSent += c
            # create a return list
            tmp = list()
            # iterate the hashmap
            for key in self.arr[ord(self.curSent[0]) - ord('a')]:
                # if the accumulated characters are the subset and starts at the beginning of the keys
                if self.curSent in key and key.index(self.curSent) == 0:
                    # append to the return list
                    tmp.append((key, self.arr[ord(self.curSent[0]) - ord('a')][key]))

            # sort the return list by frequency and ascii order
            tmp.sort(key=lambda s: (-(s[1]), s[0]))
            # # return three recommendations
            return [t[0] for t in tmp][:3]
