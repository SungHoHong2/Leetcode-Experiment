### Binary Tree Maximum Path Sum
**Recursion**
- Concepts
    - Case1: Create a maximum total sum including the parent node 
    - Case2: Create a maximum total sum excluding the parent node 
    ![image](images/Recursive.png)
- [Source code](source/Recursion.py)
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def bsearch(node):
            # return 0 if it reached the leaf
            # get the maximum score from the left branch 
            # get the maximum score from the right branch 
            # update the highest score gained from the complete path
            # return the largest possible path that starts from the leaf to the current node
            pass
        # set a global variable to keep track of the maximum sum
        # run the recursion
        # return the maximum sum
        pass
```