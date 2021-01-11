### Word Break
**Top Down**
- [Concepts](images/memoization.png)
- [Source code](source/Memoization.py)
- Time complexity `O(n^3)`
    - `O(n)`: iterate the wordDict 
    - `O(n^2)`: the size of the recursion tree is `n^2` in worst case
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # create a list that will be used for memoization
        # set the inputs as global
        # invoke the recursion
        pass

    def topdown(self, start, dp):
        # return true if the recursion reaches the leaf
        # return the record if a record is found
        # iterate from start to the end
            # if the substring matches with the wordDict and recursion no mismatches afterwards
                # record the result as true
                # return True
        # if nothing found cache the memo with False
        # return False
        pass
```

**Bottom Up**
- [Concepts](images/dp.png)
- [Source code](source/Dp.py)
```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        # set up the dp table
        # iterate the string
            # iterate the substring backwards
                # if the current word is valid and the previous substrings are valid
                    # set the dp table to true
                    # ignore the rest of the substrings
        # return the final result of the record
        pass
```

**BFS**
- [Concepts](images/bfs.png)
- [Source code](source/BFS.py)
```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        # set up a queue to search all the substrings
        # set the record of visited for the substrings
        # append the queue with the starting point zero
        # loop until the queue is depleted
            # pop the next beginning index of the substring
            # if the substring is not visited
                # iterate the substring
                    # if the substring is part of the wordDict
                        # append the the end index to the queue
                        # if end index reached the final index of the string
                            # return true
                # record the substring as visited
        # return false if there are no branches that will create all valid substrings
        pass 
```

 