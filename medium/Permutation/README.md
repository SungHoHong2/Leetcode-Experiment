### Permutations
**Backtracking**
- [Concepts](images/backtracking.png)
    - Generate all possible cases in the leaves of the recursion tree
- [Source code](source/backtracking.py)
```python
class Solution:
    def permute(self, nums):
        # globalize the input
        # return the possible permutations
        pass

    def backtrack(self, i):
        # return the result if all indexes are used for swapping
        # set the array to store the possible permutation
        # iterate all the indexes that can be swapped with the selected index
            # swap the index with the selected index
            # invoke the next recursion with the using the next index
            # recover the swapped array to its original state
        # return the possible permutations  
        pass
```