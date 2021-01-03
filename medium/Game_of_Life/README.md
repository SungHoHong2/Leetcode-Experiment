### Game of Life
- Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
    1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by over-population.
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

**O(mn) Space Solution**
- [Source code](source/Space1.py)
```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # set the up the list of eight directions of the cell
        # set the length of row and column 
        # iterate the board
                # set the temporary variable to count the neighbors
                # scan all the neighbors of the cell
                    # if the index does not exceed the board and the cells are alive
                        # increase the number of neighbor
                # if the current cell is alive and the neighbors are not 2 or 3
                    # the current cell dies
                # if the current cell is dead and the total number of neighbors are 3
                    # the current cell lives
        pass
```

**O(1) Space Solution**
- [Source code](source/Space2.py)
```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # set the up the list of eight directions of the cell
        # set the length of row and column 
        # copy the board used for checking the previous status
        # iterate the board
                # set the temporary variable to count the neighbors
                # scan all the neighbors of the cell
                    # if the index does not exceed the board and the cells are alive
                        # increase the number of neighbor
                # if the current cell is alive and the neighbors are not 2 or 3
                    # the current cell dies
                # if the current cell is dead and the total number of neighbors are 3
                    # the current cell lives
        # update the -1 and 2 to get the correct return value
        pass
```

**Infinite Board**
- Concept
    - Assume that the live cells are very sparsely distributed in the board
        - Reduce the computation by using only the live cells to get the next live cells
    - Avoid allocating the entire board in memory 
        - Allocate one row at a time when updating the board
- [Source code](source/Infinite.py)
```python 
class Solution:
    def iteration(self, live):
        # set the hashmap to count the number of lives cells for the current cell
        # set the directions for the neighbor
        # iterate the live cells
            # get the neighbors of current live cell
                # increase the number of existing neighbors
        # set up the hashset that collects the future live cells 
        # iterate the neighbors of the live cell 
            # if the cell is alive with 2 live neighbors or have 3 live neighbors
                # add the index of the live cell
        # return the future live cells
        pass

    def gameOfLife(self, board: List[List[int]]) -> None:
        # set the length of the row and column
        # set up the hashset to store the indexes of the live cell
        # return the alive cells after running the iteration function
        # allow one row of the board in memory when updating the live cell
        pass
```
