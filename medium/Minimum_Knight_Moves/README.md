### Minimum Knight Moves
**BFS**
- [Source code](source/BFS.py)
```python
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # create a BFS queue that contains (x,y,steps)
        # append the original position with zero steps
        # set a hashmap for visited
        # loop until the queue is depleted
            # pop the position and the steps
            # return the number of steps if it is equal to the destination
            # search the direction
                # if the destination is unvisited and the index is within the boundaries
                    # mark the position to the visited
                    # append the position and increase the number of steps
        # return -1 if BFS fails to reach the destination
        pass
```

**BFS + Pruning**
- [Source code](source/BFS2.py)
```python
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # create a BFS queue that contains (x,y,steps)
        # append the original position with zero steps
        # set the destination to absolute to reduce the searching space
        # set a hashmap for visited
        # loop until the queue is depleted
            # pop the position and the steps
            # return the number of steps if it is equal to the destination
            # search the direction except (-1, -2) and (-2, -1) since the destination is absolute
                # if the destination is unvisited and the index is within the reduced search space
                    # mark the position to the visited
                    # append the position and increase the number of steps
        # return -1 if BFS fails to reach the destination
        pass
```

**Two direction BFS**
- [Source code](source/BFS3.py)
```python
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # set the BFS queue that starts from the origin
        # set the BFS queue that starts from the destination
        # set visited hashmap for both BFS queues
        # iterate
            # pop the position from the first queue
            # return the steps if first BFS meets the second BFS
            # pop the position from the second queue
            # return the steps if second BFS meets the first BFS
            # iterate the possible directions
                # append the unvisited positions and increase the steps of the first BFS
                # append the unvisited positions and increase the steps of the second BFS
        # return -1 if BFS fails to reach the destination
        pass
```