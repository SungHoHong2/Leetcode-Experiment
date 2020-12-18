### Minimum Cost Tree From Leaf Values
**Remove from the smallest**
- [Concepts](images/Smallest.png)
    - Combine the smallest neighboring leaves to get the smallest possible sum 
- [Source code](source/Smallest.py)
```python
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # set the variable to return the sum of non-leaf nodes
        # loop until the array is depleted
            # get the index of the smallest element in the array
            # get the neighboring leaves of the smallest leaf
            # pop the smallest leaf
            # accumulate the result by multiplying the smallest with the smallest neighboring leaf
        # return the accumulated result 
        pass
```

**Stack**
- [Concepts](images/Optimized.png)
    - Apply stack to combine the smallest neighboring leaves to get the smallest possible sum  
- [Source code](source/Optimized.py)
```python
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # set the variable to return the sum of non-leaf nodes
        # append infinite value to the stack
        # iterate the items from the input
            # loop when the current item is bigger than the latest item
                # pop the latest item
                # get the neighboring items
                # multiply with the smallest neighbor and accumulate the result
            # append the elements according to the descending order
        # since the array is ordered, multiply from right to left
        # return the accumulated result
        pass 
```
