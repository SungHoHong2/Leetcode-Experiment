### Search in Rotated Sorted Array
**Binary search**
- Concepts
    1. Run the binary search for finding the rotation index
    1. If not rotated, search the whole array using binary search
    2. If rotated, search left or right half of the array that contains the target
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
        pass               

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
        pass
                
    def search(self, nums, target):
        # get the total length of nums
        # if there are no numbers  
            # return -1 
        # if there is a single number 
            # return zero if the single number matches with the target otherwise -1
        # find the rotate_index in the array = rotate_index 
        # if target is the rotate_index 
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
        pass
```

**One-pass Binary Search**
- Concepts
    1. Add additional condition checks in the normal binary search
    2. When finding the target using the binary search
        - If pivot value is larger than the left value in the array
            - Subarray from left to the pivot is non-rotated
            - Subarray from the pivot to the right contains a rotation
        - If pivot element is smaller than the first element of the array
            - Subarray from the pivot to the right is non-rotated
            - Subarray from the left to the pivot contains a rotation
       
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
            # if no rotation found between start and middle
                # search the leftside if target is in the leftside 
                # search rightside if target is in the rightside 
            # if no rotation found between middle and end
                # search rightside if the target is in the rightside 
                # search leftside if the target is in the leftside
        # return -1 if no target is found in the array
        pass
```
