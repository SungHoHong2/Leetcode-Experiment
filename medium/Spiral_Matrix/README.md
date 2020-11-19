### Spiral Matrix

**Simulation**
- Concepts
    - Create an additional matrix to keep track of visited cells 
    - Explore the matrix by following the spiral direction 
- [Source code](source/Simulation.py)
```python
class Solution(object):
    def spiralOrder(self, matrix):
        # if the matrix is empty
            # return a empty row
        # get the number of rows and cols
        # create the matrix for checking the visited cells
        # initialize a list for return
        # set the order of direction for the row (down,up)
        # set the order of direction for the column (right,left)
        # initalize the pointers for the direction
        # iterate the total number of cells in the matrix
            # append the current cell
            # set the current cell visited
            # move the current cell using the current direction (right,down,left,up)
            # if the cell is within the matrix and it is not visited
                # follow the current direction
            # if the cell exceeds the matrix
                # change the direction
                # update the current cell
        # return the answer
        pass
```

**Layer-by-Layer**
- Concept
    - Refrain from using the visited table 
    - Follow the concept of peeling the outer-layers while exploring the matrix
- [Source code](source/Layer.py)
```python
class Solution(object):
    def spiralOrder(self, matrix):
        # set the list for return
        # if the matrix is empty
            # return empty array
        # set the length of the row and the column
        # set the pointer for iteration and the maximum number of interation
        # set the start point of the row and column
        # iterate the total number of matrix
        # two iterations cover one layer of the matrix
            # even number of iteration
                # collect the top side of the layer
                # collect the right side of the layer
                # shrink the layer
            # odd number of iteration
                # collect the bottom side of the layer
                # collect the left side of the layer
                # shrink the layer
            # increase iteration
        # return the list
        pass
```
