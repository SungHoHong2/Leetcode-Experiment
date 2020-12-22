### Find Median from Data Stream

**Insertion Sort + Binary Search**
- [Concepts](images/)
- [Source code](source/InsertionBinary.py)
```python
class MedianFinder:

    def __init__(self):
        # set an global array 
        pass
        
    def addNum(self, num: int) -> None:
        # simply append the input if the array is empty 
        # run the binary search until left and right converges 
            # insert next to the pivot if the input is equal to the pivot  
        # if the input is larger than the whole array ex) [_,_,_,_,_,L] + [x] 
        # if the input belongs in the middle of the array ex) [_,_,_,_,_,x,L]  
        pass

    def findMedian(self) -> float:
        # return the median
        pass
```

**Two Heaps**
- [Concepts](images/)
    - Maintain direct access to median elements at all times
        - Apply max-heap to store the smaller half of the input numbers
        - Apply min-heap to store the larger half of the input numbers
- [Source code](source/TwoHeaps.py)
```python
class MedianFinder:
    def __init__(self):
        # set a max-heap that stores the smaller half of the numbers
        # set a min-heap that stores the larger half of the numbers
        pass 
    
    def addNum(self, num: int) -> None:
        # balance the max=heap and minheap so that max-heap can store one more element than min heap 
        pass
        
    def findMedian(self) -> float:
        # if the total length of the numbers are odd 
            # return the result from the max-heap 
        # if the total length of the numbers are even 
            # return the median computed from both max-heap and min-heap
        pass
```

