class AutocompleteSystem:

    def __init__(self, sentences, times):
        # create a Trie and store the input
        self.trie = dict()
        for sent, time in zip(sentences, times):
            self.createTrie(sent, time)
        # set the global head of the Trie
        self.node = self.trie
        # set global variable of the ongoing search
        self.sent = ""

    def createTrie(self, sent, time):
        # create a Trie using characters from input
        cur = self.trie
        for ch in sent:
            if ch not in cur:
                cur[ch] = dict()
            cur = cur[ch]
        # record the frequency at the finishing sentence
        cur["#"] = time

    def appendTrie(self, cur):
        # increase the frequency the new or existing sentence in the Trie
        if "#" not in cur:
            cur["#"] = 0
        cur["#"] += 1

    def dfs(self, cur, path, ans):
        # explore append all the finishing sentence to the returning list
        if "#" in cur:
            ans.append((path, cur["#"]))
        for ch in cur:
            if ch == "#": continue
            self.dfs(cur[ch], path + ch, ans)

    def input(self, c):
        # if search is finished, add a new sentence in the Trie
        if c == "#":
            self.appendTrie(self.node)
            self.node = self.trie
            self.sent = ""
            return []
        # accumulate the input
        self.sent += c
        # explore deeper or create a new leaf in the Trie
        if c not in self.node:
            self.node[c] = dict()
        self.node = self.node[c]
        # set a list to collect the possible candidates
        ans = []
        # explore the candidates using dfs
        self.dfs(self.node, self.sent, ans)
        # return the at most three best candidates
        return [s[0] for s in sorted(ans, key=lambda x: (-x[1], x[0]))[:3]]
