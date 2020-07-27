### Happy Number 

**Detect Cycles with a HashSet**
- [source code](source/hashset.py)
```python
class Solution(object):
    # function for generating the next number 
    def getNext(self, n):
        # set up the return value
        # loop until n is depleted by dividing with ten
            # get the remainder     
            # update the n with the quotient
            # add the results of the remainder
        # return the added results 
        
    def isHappy(self, n):
        # create a hash set
        # if n is not 1 and n is not in the hashset 
            # add a number in hashset
            # generate the next number
        # return true if the final result is 1 
```

**Floyd's Cycle-Finding Algorithm**
- [source code](source/floyd.py)
```python
class Solution(object):
    
    # function for finding the next number 
    def getNext(self, n):
        # set up the return value
        # loop until n is depleted by dividing with ten
            # get the remainder     
            # update the n with the quotient
            # add the results of the remainder
        # return the added results 
    
    def isHappy(self, n):
        # set up the slow number 
        # set up the fast number that goes one step ahead of the slow number        
        # loop until fast reach 1 or slow and fast meets a cycle 
            # slow moves one step at a time 
            # fast moves two steps at a time 
        # return if fast returns 1 
```
