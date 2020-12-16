class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        # return 0 if the endword is not in the wordlist
        if endWord not in wordList:
            return 0
        # set the total length of the words
        wordLength = len(beginWord)
        # set the map to hold combination of words that can be formed
        wordMap = collections.defaultdict(list)
        # iterate the words from the input
        for word in wordList:
            # check all possible combinations by iterating the total length of the word
            for i in range(wordLength):
                # store the intermediate words as the key and append the word as the value
                wordMap[word[:i]+'*'+word[i+1:]].append(word)
        # create and append the beginWord and the number of changes in the queue
        queue = collections.deque([(beginWord,1)])
        # set a map to track the visited word
        visited = dict()
        # start the BFS until it reaches the endWord
        visited[beginWord] = True
        while queue:
            # pop from the queue
            word, level = queue.popleft()
            # check all possible combinations by iterating the total length of the word
            for i in range(wordLength):
                # get the intermediate words for current word
                intermediate = word[:i]+'*'+word[i+1:]
                # get all the possible candidates from the map
                for nextWord in wordMap[intermediate]:
                    # return the total number of changes if the word reached the goal
                    if nextWord == endWord:
                        return level + 1
                    # if the converted word is not yet visited
                    if nextWord not in visited:
                        # mark the converted word as visited
                        visited[nextWord] = True
                        # add the converted word to the queue
                        queue.append((nextWord, level+1))
        # return 0 if the word cannot converted to its goal
        return 0