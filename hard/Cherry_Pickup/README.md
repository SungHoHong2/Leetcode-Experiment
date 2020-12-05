### Cherry Pickup
**General Approach**
- We can use dynamic programming to find the most number of cherries `dp[i][j]` 
- that can be picked up from any location `(i, j)` to the bottom right corner.
- Choose the move that allows us to pick up more cherries (based on comparing `dp[i+1][j]` and `dp[i][j+1]`)

**Top Down**
- Concepts
    - Avoid walking **twice** by allowing a two person walking from different direction
    - Suppose after `t` steps, the position is `(r, c)`
        - if we are starting from `(0,0)`, the number of steps implies `r + c = t`
    - Suppose two people are at positions `(r1, c1)` and `(r2, c2)` after `t` steps 
        - `r1 + c1 = r2 + c2` then `r2 = r1 + c1 - c2`
        - variables `r1, c1, c2` uniquely determine 2 people who have walked the same `r1 + c1` number of steps.
    - `dp[r1][c1][c2]` is the most number of cherries obtained by two people starting at `(r1, c1)` and `(r2, c2)`
        -  walking towards `(N-1, N-1)` picking up cherries, where `r2 = r1 + c1 - c2`
- [Source code](source/TopDown.py)
```python
class Solution(object):
    def dp(self, grid, r1, c1, c2):
        # calculate the r2
        # set the total length
        # return infinite if the row and columns of the two person reach the limit or meet the thorns
        # return the result if one person reached the destination
        # use memoization if it is visited area
        # if it is the unexplored area
            # pick the cherry from one person and the second person if it is not the same
            # recursively collect the maximum result
        # use memoization to store the visited area
        pass

    def cherryPickup(self, grid):
        # initiate the table for dp[r1][c1][c2]
        # return the result of the recursive function
        pass
```

**Bottom Up**
- [Concepts](images/BottomUp.png)
    - Suppose `r1 + c1 = t` is the `t layer`
- [Source code](source/BottomUp.py)
```python
class Solution(object):
    def cherryPickup(self, grid):
        # get the total length of the grid (row == col)
        # set the 2D table
        # start from the beginning
        # explore all the cells
            # set the temporary dp table
            # explore all possible directions of the two persons for each step
                    # if one of the person meet a thorn
                    # collect the cherry from the first person
                    # add the second person if the he explored different location
                    # accumulate the result from the 'concluded' dp table
                    # note that before completing the first half of the dp table, there is an unncessary update)
            # conclude the dp table
        # return the total collected cherries from the dp table
        pass
```