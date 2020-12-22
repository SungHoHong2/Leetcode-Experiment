### Jump Game II

**Greedy**
- [Concepts](images/)
    - To minimize the number of jumps
    - Follow the "greedy" strategy and choose the longest possible jump
    - Repeat the process again and again, till we reach the last index.
- [Source code](source/Greedy.py)

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        # return 0 if there is only one item in the input
        # get the destination
        # set a variable to record the valid coverage and the index of the last jump
        # set a counter for the number of jumps
        # apply greedy strategy that finds the largest coverage
            # record the furthest possible jump
            # the current position equals to the furthest jump
                # update last jump index
                # update counter of jump by +1
                # return the number of jumps once the current coverage covers the destination
        pass
```