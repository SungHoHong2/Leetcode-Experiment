### Burst Balloons
**Top Down**
- [Concepts](images/bottomUp.png)
    - Define a function dp to return the maximum number of coins obtainable on the open interval (left, right).
    - Base case 
        - No integers on our interval `(left + 1 == right)`
        - There are no more balloons that can be added.
    - Best score 
        - `nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right)`
- [Source code](source/TopDown.py)
```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # reframe the problem
        # set a cache
        def dp(left, right):
            # no more balloons can be added
            # return the cached results if already explored
            # add each balloon on the interval and return the maximum score
            pass
        # find the maximum number of coins obtained from adding all balloons
        pass
```

**Bottom Up**
- [Concepts](images/bottomUp.png)
    - Start running the dp from the rightmost side
- [Source code](source/BottomUp.py)
```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # reframe the input 
        # get the total length of the input
        # set the dp table that stores maximum score for within the range of left and right
        # start computing the dp from the rightmost side
        # return the largest score between the first and the last balloon
        pass
```
