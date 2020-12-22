class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.prefix_dict = collections.defaultdict(list)
        self.freq_dict = collections.defaultdict(int)
        N = len(sentences)
        for i in range(N):
            self.freq_dict[sentences[i]] = times[i]
            for j in range(1, len(sentences[i]) + 1):
                self.prefix_dict[sentences[i][:j]].append(sentences[i])
        self.sentence = ''

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            if self.sentence not in self.freq_dict:
                for j in range(1, len(self.sentence) + 1):
                    self.prefix_dict[self.sentence[:j]].append(self.sentence)
            self.freq_dict[self.sentence] += 1
            self.sentence = ''
            return []
        self.sentence += c
        if self.sentence not in self.prefix_dict:
            return []
        self.prefix_dict[self.sentence].sort(key=lambda s: (-self.freq_dict[s], s))
        return self.prefix_dict[self.sentence][:3]