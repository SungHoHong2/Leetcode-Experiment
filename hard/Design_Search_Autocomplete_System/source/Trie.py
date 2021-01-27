class AutocompleteSystem:

    def __init__(self, sentences, times):
        # create a Trie and store the input
        self.trie = dict()
        for sent, time in zip(sentences, times):
            self.createTrie(self.trie, sent, time)
        # set the global head of the Trie
        self.layer = self.trie
        # set global variable of the ongoing search
        self.curr = ""

    def createTrie(self, layer, sent, time):
        # create a Trie using characters from input
        for char in sent:
            if char not in layer:
                layer[char] = dict()
            layer = layer[char]
        # record the frequency at the finishing sentence
        layer["#"] = time

    def addTrie(self, layer):
        # increase the frequency the new or existing sentence in the Trie
        if "#" not in layer:
            layer["#"] = 0
        layer["#"] += 1

    def dfs(self, layer, path):
        # set up a returning array
        ans = list()
        # collect the results if the layer consists a word
        if "#" in layer:
            ans.append((path, layer["#"]))
        # explore deeper
        for char in layer:
            if char == "#":
                continue
            ans += self.dfs(layer[char], path + char)
        # return the matched candidates
        return ans

    def input(self, c):
        # if search is finished
        if c == "#":
            # create a new sentence in Trie
            self.addTrie(self.layer)
            # reset the trie back to the top layer
            self.layer = self.trie
            # reset the accumulating sentence
            self.curr = ""
        # if ongoing search
        else:
            # accumulate the char to the current sentence
            self.curr += c
            # explore deeper or create a new leaf in the Trie
            if c not in self.layer:
                self.layer[c] = dict()
            self.layer = self.layer[c]
            # collect the array of candidates that holds the current sentence as a first subset
            ans = self.dfs(self.layer, self.curr)
            # sort the result
            ans.sort(key=lambda x: (-x[1], x[0]))
            # return the at most three best candidates
            return [s[0] for s in ans[:3]]