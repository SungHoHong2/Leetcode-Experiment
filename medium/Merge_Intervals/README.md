### Merge Intervals
**Sorting**
- [Source code](source/Sorting.py)
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals based the starting point
        # set the return list appended with the first interval
        # iterate through the intervals
            # if the previous interval does not overlap with the current interval
                # append to the return list
            # if the previous interval overlaps with the current interval
                # merge the current interval with the previous interval
        # return the result
        pass
```

**MergeSorting the TreeNode**
- Solution without sorting, because:
    - To add intervals and merge them for a large stream of intervals
- Why use middle for comparison and not start or end boundaries?
    - Can use merge-sort technique to query the merged intervals result when the left subtree does not overlap with the right subtree.    
- [Source code](source/TreeMergeSort.py)
```python
class TreeNode:
    def __init__(self, start, end):
        # set starting point
        # set ending point
        # get the middle point
        # set the pointers for the child nodes
        pass
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # return empty list if there is no intervals
        # set root node with the first interval
        # iterate the intervals
            # append the node to the TreeNode
        # return the result of the TreeNode
        pass
    def add(self, node, new):
        # if the new end is smaller than current middle
            # if there is left child
                # append the node to the left child
            # if there is not left child
                # create new left child
        # if the start pointer is bigger than the middle
            # if there is a right child
            # if there is no right child
        # if the new start or end overlaps the current middle
            # update the start time
            # update the end time
        pass
    def query(self, node):
        # set the return variable
        # return the empty result if the node is empty
        # get the array from the left and the right child
        # iterate the left intervals
            # if the left intervals do not overlap with the current node
                # append the interval to the return array
            # if the left intervals overlap with the current node
                # merge the interval with the current node
                # break to skip appending the future nodes that overlaps with the current node
        # append the current node to the return array
        # iterate the right intervals
            # if the right interval does not overlap with the current interval
                # append the interval to the return array
            # if the right interval overlaps with the current interval
                # merge the interval with the rightmost interval in the return array
        # return the result array
        pass
```


