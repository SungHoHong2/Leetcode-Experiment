class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        # return 0 if the endWord is not in the wordList
        if endWord not in wordList:
            return 0
        # set the map to hold combination of words that can be formed
        wordMap = collections.defaultdict(list)
        # iterate the words from the input
        for word in wordList:
            # check all possible combinations by iterating the total length of the word
            for i in range(len(beginWord)):
                # store the intermediate words as the key and append the word as the value
                wordMap[word[:i]+'*'+word[i+1:]].append(word)
        # create and append the beginWord and the number of changes in the queue
        queue = collections.deque([(beginWord, 1)])
        # set a hashset to track the visited word
        visited = set()
        # start the BFS until it reaches the endWord
        while queue:
            # pop from the queue
            word, level = queue.popleft()
            # check all possible combinations by iterating the total length of the word
            for i in range(len(word)):
                # get all the possible changes from the current word
                for nextWord in wordMap[word[:i]+'*'+word[i+1:]]:
                    # return the total number of changes if the word reached the goal
                    if nextWord == endWord:
                        return level + 1
                    # if the converted word is not yet visited
                    if nextWord not in visited:
                        # mark the converted word as visited
                        visited.add(nextWord)
                        # add the converted word to the queue
                        queue.append((nextWord, level + 1))
        # return 0 if the word cannot converted to its goal
        return 0