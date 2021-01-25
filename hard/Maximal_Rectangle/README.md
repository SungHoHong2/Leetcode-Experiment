### Problem Title
**DP**
- [Concepts](images/Histogram.png)
    - Compute the maximum width to convert the input into a set of histograms
    - Compute the maximal area for each histogram
- [Source code](source/Histogram.py)
```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # set the variable to record the maximum area
        # set a dp table
        # iterate the row of the dp table
            # iterate the col of the dp table
                # continue if the area is not valid
                # record the length of the valid width
                # iterate the row from bottom to top
                    # get the height
                    # get the width
                    # record the maximum area
        # return the maximum area
        pass
```

**Stack**
- Concepts
    - Apply solution from the previous solution `Maximal Rectangle`
- [Source code](source/Stack.py)
```python
class Solution:
    # Get the maximum area in a histogram given its heights
    def leetcode84(self, height):
        # height append 0 in case there is no input
        # set a stack that will never be empty
        # set the returning answer
        # iterate the input
            # if the current height is smaller than the head of the stack
                # get the hieght
                # get the widith
                # record the maximum area
            # add the height
        # return the largest area
        pass

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # return 0 if there is no input
        # set a variable for recording the maximum area
        # set up a dp table
        # iterate the row of the matrix
            # iterate the col of the matrix
                # accumulate the maximum width from the previous row
            # update maxarea
            pass
```

**Maximum Height at Each Point**
- [Concepts](images/)
- [Source code](source/MaxHeight.py)
```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # return 0 if there is no input
        # get the length of the rows
        # get the length of the columns
        # set the dp table for left, right, height
        # set the variable for recording the maximum area
        # iterate the row of the input
            # set the current left and right
            # accumulate the height for each columns or set as invalid 
            # update the available left index 
                # maintain the maximum width if the height is valid 
                # reduce the maximum width if the height is invalid        
            # update the available right index 
                # maintain the maximum width if the height is valid
                # reduce the maximum width if the height is invalid                 
            # update the area
                # compute the area if the height is valid        
        # return the maximum area
        pass
```
