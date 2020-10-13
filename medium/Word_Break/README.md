### Word Break
**Recursion with memoization**
- [Concepts](images/memoization.png)
- [Source code](source/Memoization.py)
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # create a list of to record the results of the substring
        # invoke the recursion
        pass

    def bruteBreak(self, s, wordDict, start, memo):
        # if the recursion reaches the leaf
            # return as True
        # if a record is found
            # return the result from the record
        # iterate from start to the end
            # if the substring matches with the wordDict and recursion no mismatches afterwards
                # record the result as true
                # return True
        # if nothing found cache the memo with False
        # return False
        pass 
```


**Using Breadth-First-Search**
- [Concepts](images/bfs.png)
- [Source code](source/BFS.py)
```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        # convert the wordDict to set
        # set up a queue to search all the substrings
        # set the record of visited for the substrings
        # append the queue with the starting point zero
        # loop until the queue is depleted
            # pop the next begining index of the substring
            # if the substring is not visited
                # iterate the substring
                    # if the substring is part of the wordset
                        # append the the end index to the queue
                        # if end index reached the final index of the string
                            # return true
                # record the substring as visited
        # return false if there are no branches that will create all valid substrings
        pass 
```

**Using Dynamic Programming**
- [Concepts](images/dp.png)
- [Source code](source/Dp.py)
```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        # set up a list to record the substrings
        # iterate the string
            # interate the substring backwards
                # get teh sbustring
                # check the validity of the previous substring
                # if the current word is valid and the previous substrings are valid
                    # return true
                    # no need to check the rest of the substrings
        # return the final result of the record
        pass 
```
 