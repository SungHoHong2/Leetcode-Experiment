### Best Time to Buy and Sell Stock
**One Pass**
- [source code](source/one_pass.py)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set the tracker for the most minimum price 
        # set the maximum profit (return value)
        # iterate the available prices 
            # keep track of the lowest minimum price 
            # keep track of the highest maximum profit  
        # return the maximum profit
```
**Kadane's algorithm**
- the algorithm for getting the `largest sum` of the `contiguous subarray`
- [source code](source/one_pass.py)

```python
# max_so_far = 0 
# max_ending_here = 0  
# loop for each element of the array 
    # max

```