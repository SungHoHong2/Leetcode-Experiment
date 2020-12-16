class Solution(object):
    def visitWordNode(self, queue, visited, others_visited):
        # pop from the queue
        word, level = queue.popleft()
        # check all possible combinations by iterating the total length of the word
        for i in range(self.wordLength):
            # get the intermediate words for current word
            intermediate = word[:i] + '*' + word[i+1:]
            # get all the possible candidates from the map
            for nextWord in self.wordMap[intermediate]:
                # If the interediate word is already visited by the other BFS
                if nextWord in others_visited:
                    # return the current number of conversions + conversions from other BFS
                    return level + others_visited[nextWord]
                # if the converted word is not yet visited
                if nextWord not in visited:
                    # save the words in the map with the number of conversions
                    visited[nextWord] = level + 1
                    # add the converted word to the queue
                    queue.append((nextWord, level+1))
        # return null if nothing is found
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        # return 0 if the endword is not in the wordlist
        if endWord not in wordList:
            return 0
        # set the total length of the words
        self.wordLength = len(beginWord)
        # set the map to hold combination of words that can be formed
        self.wordMap = collections.defaultdict(list)
        # iterate the words from the input
        for word in wordList:
            # check all possible combinations by iterating the total length of the word
            for i in range(self.wordLength):
                # store the intermediate words as the key and append the word as the value
                self.wordMap[word[:i]+'*'+word[i+1:]].append(word)
        # create queue that starts the BFS from the beginWord
        topQueue = collections.deque([(beginWord,1)])
        # create queue that starts the BFS from the endWord
        bottomQueue = collections.deque([(endWord,1)])
        # set a map to track the visited word for the two BFS
        topVisited, bottomVisited = dict(), dict()
        # loop until one of the BFS is finished
        topVisited[beginWord] = 1
        bottomVisited[endWord] = 1
        while topQueue and bottomQueue:
            # explore from the top
            ans = self.visitWordNode(topQueue, topVisited, bottomVisited)
            # return the number of transformation if the answer is found from the top
            if ans:
                return ans
            # explore form the bottom
            ans = self.visitWordNode(bottomQueue, bottomVisited, topVisited)
            # return the number of transformation if the answer is found from the bottom
            if ans:
                return ans
        # return 0 if nothing is found
        return 0