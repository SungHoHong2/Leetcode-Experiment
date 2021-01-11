### Coin Change
**Top down**
- [Concept](images/dp.png)
    - Provide an optimal substructure property
- [Source code](source/Topdown.py)
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # set the coins as a global variable 
        # set up the dp table to record the number of required coins according to the amount 
        # base case: when the amount is zero then amount of required coins is zero
        # collect the answer from the top down
        # return the answer or -1 if the coins do not sum up to the amount 
        pass
       
    def topdown(self, dp, remain):
        # return infinite if the coins do not sum up to the amount
        # return the recorded result if the answer is cached in the dp table 
        # set the variable to record the minimum number of coins
        # iterate the coins
            # get the smallest number of coins that sum up to the remaining amount
        # update the number of coins that sum up to the amount in the dp table
        # return result
        pass
```

**Bottom up**
- [Concepts](images/Bottomup.png)
- [Source code v2](source/Bottomup2.py)
- [Source code](source/Bottomup.py)
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # set the array to record the results of each amount
        # if total amount is zero there is zero coins
        # iterate the coins
            # iterate the amount that fits into the current coin
                # update the answer by adding or without the coins
        # return the minimum number of coins or -1 if invalid
        pass
```