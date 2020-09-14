### Search in Rotated Sorted Array
**Binary search**
- [Source code](source/Binary.py)
```python
class Solution:
    def find_rotate_index(self,nums, left, right):
        # if first element is smaller than the last element
            # there was no rotation in the array 
        # loop until the whole array is searched 
            # get the middle pivot
            # if the pivot is larger than the rightside neighbor
            #            P N 
            # ex) [4,5,6,7,0,1,2]
                # return the index of the right side
            # if the pivot is smaller than the left side
            #            L   P   R
            # ex) [4,5,6,7,0,1,2,3]            
                # search for the left area
            # if the pivot is larger than the left side
            #        L   P   R
            # ex) [4,5,6,7,0,1,2,3]               
            # search for the right area                    

    def binarySearch(self,nums, target, left, right):
        # loop until the whole array is searched 
            # get the middle pivot
            # if the pivot matches the target 
                # return the pivot 
            # if the pivot is larger than the target
                # search the left area of the array 
            # if the pivot is smaller than the target
                # search for the right area of the array 
        # return -1 if there is no target in the array 
                
    def search(self, nums, target):
        # get the total length of 
        # if there are no numbers  
            # return -1 
        # if there is a single number 
            # return zero if the single number matches with the target otherwise -1
        # find the smallest elemement in the array = rotate_index 
        # if target is the smallest element 
            # return the rotate_index 
        # if array is not rotated
            # perform binary search on the entire array 
        # if the target is smaller than the first element 
        # ex) [4,5,6,7,0,1,2]
        #     target = 2 first = 4 
            # search from the rotate_index
        # if the target is bigger than the first element
        # ex) [4,5,6,7,0,1,2]
        #     target = 6 first = 4 
        # search until the rotate_index 
```

**One-pass Binary Search**
- [Source code](source/ReferredBinary.py)
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set up the start pointer for binary search
        # set up the end pointer for binary search
        # loop until the array is completely explored
            # get the pivot
            # if the pivot is the target
                # return the index of the pivot
            # implies no rotation in the array
                #  S     M     E
                # [0,1,2,3,4,5,6]
                # if the target is smaller than the pivot
                # Target = 1
                    # search the left side of the array
                # if the target is bigger than the pviot
                # Target = 5
                    # search the right side of the array
            # implies a rotation in the array
                #  S     M     E
                # [4,5,6,0,1,2,3]
                # if the target is larget than the middle
                # Target = 1
                    # search the right side of the array
                # if the target is smaller than the middle
                # Target = 5
                    # search the left side of the array
        # return -1 if no target is found in the array

```
