### Maximal Square

- **Dynamic programming**
    - [concepts](images/dynamic1.png)
    - [source code](source/dynamic.py)
    - [reference #1](https://www.youtube.com/watch?v=RElcqtFYTm0)
```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # return 0 if there is no input
        # get the length of the rows
        # get the length of the columns
        # create a table for storing the results of the subproblems
        # set the integer to record the maximum length
        # iterate the rows
            # iterate the cols
                # if the current cell is "1"
                    # increment from the left, top, and diagonal results
                    # keep track of the maximum length of the square
        # return the size of the maximum square
        pass
```    

- **Optimal dynamic programming** 
    - [concepts](images/dynamic2.png)
    - [source code](source/dynamic2.py)
```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # return 0 if there is no matrix
        # get the length of the rows
        # get the length of the columns
        # reduce the original table to a single row
        # set the variable for tracking the maximum length
        # set the variable to track the diagonal
        # iterate the rows
            # iterate the cols
                # get the top
                # if the current cell is 1
                    # get the left
                    # update the maximum size of the square
                    # keep track of the maximum length of the square
                # update the current maximum size of the square to zero
                # get the diagonal
        # return the size of the maximum square
        pass
```
