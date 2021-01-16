### Jump Game
- Note that the dp solutions does not pass all the tests

**Top Down**
- [Concepts](images/)
- [Source code](source/TopDown.py)
```python
class Solution:
    def bottomUp(self, position, nums):
        # return the dp table if the index is explored
        # get the maximum jump of the current index 
        # iterate all the possible jumps from the current position
            # record the dp table as true if the jump reaches the destination
        # record the dp table as false
        pass

    def canJump(self, nums: List[int]) -> bool:
        # set up the dp table
        # base case: final index reaches the destination
        # invoke the bottom up approach
        pass
```

**Bottom Up**
- [Concepts](images/)
- [Source code](source/BottomUp.py)
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # set the dp table 
        # base case: final index reaches the destination
        # iterate the input backwards
            # iterate all the possible jumps from the current position 
            # record the dp table as true if the jump reaches the destination
        # return if the destination is reachable from the first index
        pass
```

**Greedy**
- [Concepts](images/)
- [Source code](source/Greedy.py)
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # set the last position
        # iterate the input backwards
            # update the last position if the possible jump can reach the last position 
        # return true if the last position reaches the starting point 
        pass
```
