### Merge Intervals
**Sorting**
- [Source code](source/Sorting.py)
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals based the starting point
        # set the return list
        # iterate through the intervals 
            # if it is the first interval or the previous interval does not overlap with the current interval
                # append to the return list 
            # if it s not the first interval and the previous interval overlaps with the current interval
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
        # set root node
        # if there is no intervals
        # iterate the intervals
            # if there is no root
                # create a root node for the TreeNode
            # if there is a root
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
        # the new start or end overlaps the current middle
            # update the start time
            # update the end time
        pass
    def query(self, node):
        # the node is empty
            # return the empty result
        # get the array from the left and the right child
        # set the return variable
        # set the flag to check whether the current node is merged with the intervals from the left
        # iterate the left intervals
            # if the left intervals do not overlap with the current node
                # append the interval to the return array
            # if the left intervals overlap with the current node
                # merge the interval with the current node and append to the return array
                # break from the iteration and skip adding the current node
        # if there was no merge of the current node
            # append the interval to the return array
        # iterate the right intervals
            # if the right interval does not overlap with the current interval
                # append the interval to the return array
            # if the right interval overlaps with the current interval
                # merge the interval with the rightmost interval in the return array
        # return the result array
        pass 
```


