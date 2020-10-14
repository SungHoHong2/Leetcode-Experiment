### Search a 2D Matrix II
**Binary Search**
- [Source code](source/Binary.py)
```python
class Solution:
    def binary_search(self, matrix, target, start, vertical):
        # set the lowest index
        # set the highest index
        # loop until the lowest index meets the highest
            # get the middle
            # if it is a horizontal search
                # binary search the columns
            # if it is a vertical search
                # binary search the rows
        # return false if no target was found
        pass 

    def searchMatrix(self, matrix, target):
        # if there is not input
            # return false

        # iterate the matrix diagonally
            # binary search the target vertically
            # binary search the target horizontally
            # if the target is found
                # return true
        # return false if the target was not found with binary search
        pass 
```

**Divide and Conquer**
- For a sorted two-dimensional array
- Base Case
    - First, if the array has zero area, it contains no elements and therefore cannot contain target.
    - Second, if targets smaller than the array's smallest element `(found in the top-left corner) or larger than the array's largest element (found in the bottom-right corner)`, then it definitely is not present.
- Recursive Case
    - If the base case conditions have not been met, then the array has positive area and target could potentially be present. 
    - Therefore, we seek along the matrix's middle column for an index row such that `matrix[row-1][mid] < target < matrix[row][mid]`
    - The existing matrix can be partitioned into four submatrice around this index
    - The `top-left and bottom-right submatrice` cannot contain target
    - The `bottom-left and top-right submatrice` are sorted two-dimensional matrices, so we can recursively apply this algorithm to them.    
 
- [Concepts](images/Divide.png)
- [Source code](source/Divide.py)
```python
class Solution:
    def search_rec(self,left, up, right, down):
        # return false if the submatrix is empty
        # return false if the `target` is not in top-left and bottom-right submatrice
        # get the pivot
        # locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            # return true if the target is found while locating the middle
        # invoke recursions for the bottom-left and the top-right submatrice
        pass 

    def searchMatrix(self, matrix, target):
        # set the target variable to global
        # set the matrix variable to global
        # if the input is empty
            # return false
        # invoke recursion
        pass 
``` 

**Search Space Reduction**
- [Source code](source/Reduction.py)
```python
class Solution:
    def searchMatrix(self, matrix, target):
        # return false if there is no input
        # start our "pointer" from the bottom-left
        # loop until the pointer reaches the top-right
            # move up if the target is smaller than the current value
            # move right if the target is larger than the current value
            # return true if found
        # return false if not found
        pass 
```
