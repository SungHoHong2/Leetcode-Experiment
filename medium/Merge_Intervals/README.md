### Merge Intervals
**Connected Components**
- [Source code](source/)

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals
        # set a flag for merge
        # loop until there is no intervals to merge
            # set the merge flag to false
            # compare all the intervals with double for-loops
                # if there is a merge break
                # inner for-loop  
                    # get the interval from i
                    # get the interval from j
                    # check if the two intervals overlap
                        # merge interval to i
                        # remove the interval of j
                        # set the merge flag to true
                        # break
        # return the result
```

**Sorting**
- [Source code](source/Sorting.py)
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals based the starting point
        # set the return list
        # iterate through the intervals 
            # if it is the first interval or the previous interval does not overlap with the current interval
                # append to merge 
            # if it s not the first interval and the previous interval overlaps with the current interval
                # merge the current interval with the previous interval
        # return the result
```

**MergeSorting the TreeNode**
- [Source code](source/TreeMergeSort.py)
```python
# declare a treenode 
class TreeNode:
    def __init__(self, start, end, middle):
        # set starting point 
        # set ending point 
        # get the middle point 
        # set the pointers for the child nodes
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # set root node
        # if there is no intervals
            # return empty list
        # iterate the intervals
            # if there is no root
                # create a root node for the TreeNode 
            # if there is a root
                # append the node to the TreeNode 
        # return the result of the TreeNode
    def add(self, node, start, end):
        # if the new end is smaller than current middle 
            # if there is left child 
                # append the node to the left child 
            # if there is not left child
                # create new left child 
        # if the start pointer is bigger than the middle 
            # if there is a right child 
            # if there is no right child 
                # create a new right child 
        # the new start or end overlaps the current middle
            # update the start time 
            # update the end time
    def query(self, node):
        # the node is empty 
            # return the empty result 
        # merge-sort divide and conquer
        # set the return variable 
        # set the inserted flag 
        # iterate the left intervals
            # if the left intervals overlap with the current node
                # create a new overlap node
                # set the inserted flag as true 
                # break from the iteration
            # if the left intervals do not overlap with the current node 
                # append the interval to the result 
        # if the inserted flag is false
            # append the head interval 
        # iterate the right intervals
            # if the right interval overlaps with the current interval 
                # update the interval from the result array
            # if the right interval does not overlap with the current interval
                # append the interval to the result 
        # return the result array 
```


