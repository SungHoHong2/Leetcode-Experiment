### Word Ladder
**Breadth First Search**
- [Source code](source/BFS.py)
```python
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        # return 0 if the endword is not in the wordlist
        # set the total length of the words
        # set the map to hold combination of words that can be formed
        # iterate the words from the input
            # check all possible combinations by iterating the total length of the word
                # store the intermediate words as the key and append the word as the value
                # (example) key:*ot value:['hot', 'dot', 'lot']
        # create and append the beginWord and the number of changes in the queue
        # set a map to track the visited word
        # loop the queue until it is depleted
            # pop from the queue
            # check all possible combinations by iterating the total length of the word
                # get the intermediate words for current word
                # get all the possible candidates from the map
                    # return the total number of changes if the word reached the goal
                    # if the converted word is not yet visited
                        # mark the converted word as visisted
                        # add the converted word to the queue
        # return 0 if the word cannot converted to its goal
        pass
```

**Bidirectional Breadth First Search**
- [Concepts](images/Bidirectional.png)
- [Source code](source/BiDirect.py)
```python
class Solution(object):
    def visitWordNode(self, queue, visited, others_visited):
        # pop from the queue
        # check all possible combinations by iterating the total length of the word
            # get the intermediate words for current word
            # get all the possible candidates from the map
                # If the interediate word is already visited by the other BFS 
                    # return the current number of conversions + conversions from other BFS 
                # if the converted word is not yet visited                
                    # save the words in the map with the number of conversions
                    # add the converted word to the queue
        # return null if nothing is found 
        pass 

    def ladderLength(self, beginWord, endWord, wordList):
        # return 0 if the endword is not in the wordlist
        # set the total length of the words
        # iterate the words from the input
            # check all possible combinations by iterating the total length of the word
                # store the intermediate words as the key and append the word as the value
        # iterate the words from the input
            # check all possible combinations by iterating the total length of the word
                # store the intermediate words as the key and append the word as the value
                # (example) key:*ot value:['hot', 'dot', 'lot']
        # create queue that starts the BFS from the beginWord 
        # create queue that starts the BFS from the endWord 
        # set a map to track the visited word for the two BFS
        # loop until one of the BFS is finished
            # hop from begin word
            # hop from end word
        # return 0 if nothing is found 
        pass
```

