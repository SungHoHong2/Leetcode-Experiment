### Happy Number 

**Detect Cycles with a HashSet**
- [Source code](source/hashset.py)
- Time complexity : **O(log(n))**(Challenging) 
- Space complexity : **O(log(n))**(Challenging) 
```python
class Solution(object):
    # function for generating the next number 
    def getNext(self, n):
        # set up the return value
        # loop until n is depleted by dividing with ten
            # get the remainder     
            # update the n with the quotient
            # add the results of the remainder powered by two 
        # return the added results 
        
    def isHappy(self, n):
        # create a hash set to record the cycle
        # loop until n is 1 or meets a cycle 
            # add a number in hashset
            # generate the next number
        # return true if the final result is 1 
```

**Floyd's Cycle-Finding Algorithm**
- [source code](source/floyd.py)
- Time complexity : **O(log(n))** 
- Space complexity : **O(1)**(Challenging) 
```python
class Solution(object):
    # function for finding the next number 
    def getNext(self, n):
        # set up the return value
        # loop until n is depleted by dividing with ten
            # get the remainder     
            # update the n with the quotient
            # add the results of the remainder powered by two 
        # return the added results 
    def isHappy(self, n):
        # set up the slow number 
        # set up the fast number that goes one step ahead of the slow number        
        # loop until fast reach 1 or slow and fast meets a cycle 
            # slow moves one step at a time 
            # fast moves two steps at a time 
        # return if fast returns 1 
```
