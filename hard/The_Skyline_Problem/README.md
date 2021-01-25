### The Skyline Problem
**Max Heap**
- [Concepts](images/)
    - Create an array that contains the `L,H,R` and the finish indicator `R,_,_`
    - Sort the buildings according to `x coordinate` 
    - Apply the `max heap` to check whether the silhouette of the building changes 
        - if the tallest height in the heap is different from the current height 
            - append red points as the result 
        - if current left index passes the tallest height in the heap
            - pop out the tallest height from the heap
         
- [Source code](source/maxHeap.py)
- [Reference #1](https://www.youtube.com/watch?v=GSBLe8cKu0s)
```python
from heapq import heappush, heappop
    
class Solution(object):
    def getSkyline(self, buildings):
        # add starting point of the building (L, -H, R)
        # add ending point of the building (R,0,0)
        # sort the events in ascending order based on the L
        # set the returning array that collects [L, height] with a starting point
        # set the max heap that collects the [-height, R]
        # iterate the building
            # get the latest building from the heap 
            # pop buildings that has ended
            # push the building to the heap
            # get the latest building from the returning array 
            # get the latest building from the heap 
            # append the result if the tallest building changes
        # return the result without the starting point
        pass
```