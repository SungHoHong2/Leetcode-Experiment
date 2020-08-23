### Game of Life
**O(mn) Space Solution**
- [Source code](source/Space1.py)
```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # set the up the list of eight directions of the cell
        # set the number of rows
        # set the number of columns
        # copy the board
        # iterate the board
                # set the temporary variable to count the neighbors
                # scan all the neighbors of the cell
                    # if the index does not exceed the board and the cells are alive
                        # increase the number of neighbor
                # if the current cell is alive and the neighbors are not 2 or 3
                    # the current cell dies
                # if the current cell is dead and the total number of neighbors are 3
                    # the current cell lives
```

**O(1) Space Solution**
- [Source code](source/Space2.py)
```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # set the up the list of eight directions of the cell
        # set the number of rows
        # set the number of columns
        # iterate the board
                # set the temporary variable to count the neighbors
                # scan all the neighbors of the cell
                    # if the index does not exceed the board and the cells are alive
                        # increase the number of neighbor
                # if the current cell is alive and the neighbors are not 2 or 3
                    # the current cell dies
                # if the current cell is dead and the total number of neighbors are 3
                    # the current cell lives
        # modfiy the -1 and 2 to get the correct return value
```

**Infinite Board**
- [Source code](source/Infinite.py)

```python 
class Solution:
    def iteration(self, live):
        # set the hashmap to count the number of lives cells for the current cell
        # set the directions for the neighbor
        # iterate the live cells
            # get the neighbors of current live cell
                # increase the number of existing neighbors
        # set up a return hashset
        # iterate the counter hashmap
            # if the exisitng neighbors are alive and have 3 or 2 live neighbors
                # add the index to the return hashset
        # return the hashhset

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # set the variable of the row
        # set the variable of the column
        # set up the hashset to store the indexes of the live cell
        # iterate the board
                # if the cell is alive
                    # add to the hashset
        # return the alive cells after running the iteration function
        # iterate the board
                # update the live cells
```
