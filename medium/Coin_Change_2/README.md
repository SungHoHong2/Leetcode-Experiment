### Coin Change 2
**Bottom Up**
- Concept
    - Knapsack problem
        - the row represents the amount from 0 to amount 
        - the column represents the coins that are used to fill the amount
- Time Complexity `O(n*amount)`
    - `n` is the number of available coins 
- [Source code](source/BottomUp.py)
```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # set up the table for keeping records of possible combinations 
        # if the amount is zero then there is one combination 
        # iterate the coins 
            # iterate the possible amount
                # accumulate previous combinations if the coin can fit into the current amount
        # return the possible number of combination to reach the result   
        pass    
```