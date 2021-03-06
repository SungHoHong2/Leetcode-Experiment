### Search a 2D Matrix II
**Binary Search**
- Concept
    - Diagonally traverse the matrix while searching both vertically and horizontally
- [Source code](source/Binary.py)
```python
class Solution:
    def binary_search(self, target, start, vertical):
        # set the lowest index
        # set the highest index for vertical or horizontal
        # loop until the lowest index meets the highest
            # get the middle
            # if it is a vertical search
                # binary search the rows
            # if it is a horizontal search
                # binary search the columns
        # return false if no target was found
        pass

    def searchMatrix(self, matrix, target):
        # return false if the matrix is empty
        # globalize the input
        # iterate the matrix diagonally
            # binary search the target vertically
            # binary search the target horizontally
            # return true if the target is found
        # return false if the target was not found with binary search
        pass
```

**Divide and Conquer**
- [Concepts](images/Divide.png)
    - Suppose there is a sorted two-dimensional array
    - Base Case
        - If the array contains no items then target cannot be matched 
        - If the target is smaller than the array's smallest item `(found in the top-left corner)` then the target does not exist
        - If the target is larger than the array's largest item `(found in the bottom-right corner)`, then the target does not exist 
    - Recursive Case
        - If the base case conditions have not been met, 
            - The target could potentially be present. 
        - Seek along the matrix's middle column for an index row `matrix[row-1][mid] < target < matrix[row][mid]`
        - The existing matrix can be partitioned into four submatrices around this index
            - The `top-left and bottom-right submatrices` cannot contain target
                - Following the idea from the `base case`
                    - Increasing the row implies that the target is bigger than the `top left`
                    - Halting at some row implies that the target is smaller than the `bottom right`
            - Search the area of `bottom-left and top-right submatrices`  

- [Source code](source/Divide.py)
```python
class Solution:
    def recursion(self, target, left, up, right, down):
        """
        target = 5
        [ 1,2,  3, [4,5]]
        [ 2,3, [4],[5,6]]
        [[3,4],[6], 8,9]
        [[4,5], 7,  8,9]
        once the target is between the two rows, the target is in down,left or top,right
        """
        # return false if the target does not exist 
        # return false if the target is within the in top-left and bottom-right submatrices              
        # get the horizontal pivot
        # get the vertical pivot == matrix[row-1][mid] < target < matrix[row][mid]
            # return true if the target is found while locating the middle
        # explore the target in the bottom-left and the top-right submatrices
        pass

    def searchMatrix(self, matrix, target):
        # set the matrix variable to global
        # return false if the input is empty
        # invoke recursion
        pass
```

**Search Space Reduction**
- Concept
    - Since the rows are sorted from left-to-right
        - every value to the right of the current value is larger 
        - If the current value is already larger than target,
            - Every value to its right will also be too large.        
    - Start from the `bottom-left` 
    - If the current value is larger than target, move one row `up`
    - If the current value is smaller than target, move one column `right` 

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
