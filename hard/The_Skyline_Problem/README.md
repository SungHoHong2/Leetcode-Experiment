### The Skyline Problem
**Max Heap**
- [Concepts](images/)
    - Create an array that contains the `L,H,R` and the finish indicator `R,_,_`
    - Sort the buildings according to `x coordinate` 
    - Apply the `max heap` to check whether the silhouette of the building changes 
        - if the height of building is smaller than it should be hidden by the taller building 
- [Source code](source/maxHeap.py)
- [Reference #1](https://www.youtube.com/watch?v=GSBLe8cKu0s)
```python
from heapq import heappush, heappop
class Solution(object):
    def getSkyline(self, buildings):
        # add starting point of the building (L, -H, R)
        # add ending point of the building events (R,0,0)
        # sort the events in ascending order based on the left
        # set the result [L, height] with a starting point
        # set the min heap to keep track of the highest height, [-height, R]
        # iterate the building
            # pop buildings that no longer valid
            # keep track of the valid building with the tallest height
            # append the result if the tallest building changes
        # return the result without the starting point
        pass
```