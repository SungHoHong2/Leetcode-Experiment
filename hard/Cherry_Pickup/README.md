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
    def topdown(self, grid, r1, c1, c2):
        # calculate the r2
        # get the total length of the grid
        # return infinite if the index exceeds or have the thorns     
        # return the result if one person reached the destination
        # return the recorded result if exists    
        # if index is the unexplored area
            # pick the cherry from one person and the second person if it is not the same
            # recursively collect the maximum result        
            # record the visited area
            # return the total number of picked cherries 
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
        # iterate all the layers
            # set the temporary dp table
            # the start of the layer increases after it moves beyond the half
            # the end of the layer stops increasing after it moves beyond the half
            # iterate the current layer 
                    # if one of the person meet a thorn
                    # collect the cherry from the first person
                    # add the second person if the he explored different location
                    # accumulate the dp table from the dp table made from the previous layer
            # save the state of the dp table 
        # return the total collected cherries from the dp table
        pass
```