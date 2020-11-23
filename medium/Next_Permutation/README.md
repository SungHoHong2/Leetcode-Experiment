### Next Permutation

**Single Pass Approach**
- [Concepts](images/Single.png)
    - Suppose that numbers with the ascending order from the right is the biggest number 
        - `54321`, `9876543210`
    - Find `pivot` which is the `descending number` from the right
        - `9876[0]43210`
    - Swap the `pivot` with the number that is larger from the right
        - `9876[0]43210`
    -     
- [Source code](source/Single.py)

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the item that has the ascending order 
        # if the pivot that has the ascending order is found 
            # find the smallest item that is from the right side of the pivot
            # swap the next larger number number with the pivot 
        # reverse all the items in the right side of the pivot
        pass 

    def swap(self, nums, i, j):
        pass 

    def reverse(self, nums, start):
        pass
```
