### Burst Balloons
**Top Down**
- Concepts
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
- [Source code](source/BottomUp.py)
```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # reframe problem as before
        # get the total length of the input
        # dp will store the results of our calls
        # expand the scope of dp from the [n-2:n] items numbers to all items [0:n]
        # return the final result of the dp [0:n]
        pass
```
