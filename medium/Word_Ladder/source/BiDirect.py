class Solution(object):

    def visitWordNode(self, queue, visited, others_visited):
        # pop from the queue
        current_word, level = queue.popleft()
        # check all possible combinations by iterating the total length of the word
        for i in range(self.length):
            # get the intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            # get all the possible candidates from the map
            for word in self.all_combo_dict[intermediate_word]:
                # If the interediate word is already visited by the other BFS
                if word in others_visited:
                    # return the current number of conversions + conversions from other BFS
                    return level + others_visited[word]
                # if the converted word is not yet visited
                if word not in visited:
                    # save the words in the map with the number of conversions
                    visited[word] = level + 1
                    # add the converted word to the queue
                    queue.append((word, level + 1))
        # return null if nothing is found
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        # return 0 if the endword is not in the wordlist
        if endWord not in wordList:
            return 0
        # set the total length of the words
        self.length = len(beginWord)
        self.all_combo_dict = collections.defaultdict(list)
        # iterate the words from the input
        for word in wordList:
            # check all possible combinations by iterating the total length of the word
            for i in range(self.length):
                # store the intermediate words as the key and append the word as the value
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        # iterate the words from the input
        for word in wordList:
            # check all possible combinations by iterating the total length of the word
            for i in range(self.length):
                # store the intermediate words as the key and append the word as the value
                # (example) key:*ot value:['hot', 'dot', 'lot']
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        # create queue that starts the BFS from the beginWord
        queue_begin = collections.deque([(beginWord, 1)])
        # create queue that starts the BFS from the endWord
        queue_end = collections.deque([(endWord, 1)])
        # set a map to track the visited word for the two BFS
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None
        # loop until one of the BFS is finished
        while queue_begin and queue_end:
            # hop from begin word
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            # hop from end word
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans
        # return 0 if nothing is found
        return 0