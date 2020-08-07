### Best Time to Buy and Sell Stock
**One Pass**
- [Source code](source/one_pass.py)
- Time complexity : **O(n)** Only a single pass is needed.
- Space complexity : **O(1)** Only two variables are used.
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
- The algorithm for getting the `largest sum` of the `contiguous subarray`
- [Concept](image/kadane.png)
- [Source code](source/kadane.py)
```python
# max_so_far = 0 
# max_ending_here = 0  
# loop for each element of the array 
    # max_ending_here = max_ending_here + a[i]
    # if max_ending_here < 0 
        # max_ending_here = 0 
    # if max_so_far < max_ending_here 
        # max_so_far  max_ending_here 
# return max_so_far 
```
```python
class Solution(object):
    def maxProfit(self, prices):
        # set up the current profit 
        # set up the maximum profit 
        # iterate the prices 
            # aggregate the current profit 
            # set the current profit to zero if it reaches negative
            # keep track of the maximum profit 
        # return the maximum profit 
```