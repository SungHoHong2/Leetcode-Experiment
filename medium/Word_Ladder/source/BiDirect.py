class Solution(object):
    def visitWordNode(self, queue, visited, others_visited):
        # pop from the queue
        word, level = queue.popleft()
        # check all possible combinations by iterating the total length of the word
        for i in range(len(word)):
            # get all the possible candidates from the map
            for nextWord in self.wordMap[word[:i]+'*'+word[i+1:]]:
                # If the intermediate word is already visited by the other BFS
                if nextWord in others_visited:
                    # return the current number of conversions + conversions from other BFS
                    return level + others_visited[nextWord]
                # if the converted word is not yet visited
                if nextWord not in visited:
                    # save the words in the map with the number of conversions
                    visited[nextWord] = level + 1
                    # add the converted word to the queue
                    queue.append((nextWord, level+1))
        # return 0 if nothing is found
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        # return 0 if the endWord is not in the wordList
        if endWord not in wordList:
            return 0
        # set the map to hold combination of words that can be formed
        self.wordMap = collections.defaultdict(list)
        # iterate the words from the input
        for word in wordList:
            # check all possible combinations by iterating the total length of the word
            for i in range(len(word)):
                # store the intermediate words as the key and append the word as the value
                self.wordMap[word[:i]+'*'+word[i+1:]].append(word)
        # create queue that starts the BFS from the beginWord
        topQueue = collections.deque([(beginWord, 1)])
        # create queue that starts the BFS from the endWord
        bottomQueue = collections.deque([(endWord, 1)])
        # set a map to track the visited word for the two BFS
        topVisited, bottomVisited = dict(), dict()
        topVisited[beginWord] = 1
        bottomVisited[endWord] = 1
        # loop until one of the BFS is finished
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