class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        # return 0 if the endword is not in the wordlist
        if endWord not in wordList:
            return 0
        # set the total length of the words
        L = len(beginWord)
        # set the map to hold combination of words that can be formed
        all_combo_dict = collections.defaultdict(list)
        # iterate the words from the input
        for word in wordList:
            # check all possible combinations by iterating the total length of the word
            for i in range(L):
                # store the intermediate words as the key and append the word as the value
                # (example) key:*ot value:['hot', 'dot', 'lot']
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        # create and append the beginWord and the number of changes in the queue
        queue = collections.deque([(beginWord, 1)])
        # set a map to track the visited word
        visited = {beginWord: True}
        # loop the queue until it is depleted
        while queue:
            # pop from the queue
            current_word, level = queue.popleft()
            # check all possible combinations by iterating the total length of the word
            for i in range(L):
                # get the intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                # get all the possible candidates from the map
                for word in all_combo_dict[intermediate_word]:
                    # return the total number of changes if the word reached the goal
                    if word == endWord:
                        return level + 1
                    # if the converted word is not yet visited
                    if word not in visited:
                        # mark the converted word as visisted
                        visited[word] = True
                        # add the converted word to the queue
                        queue.append((word, level + 1))
        # return 0 if the word cannot converted to its goal
        return 0