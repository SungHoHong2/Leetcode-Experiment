### Next Permutation

**Single Pass Approach**
- [Concepts](images/Single.png)
    - Suppose that numbers with the ascending order from the right is the biggest number 
        - `9876543210`
    - Find `pivot` which is the `descending number` from the right
        - `9876043210` -> `9876[0]43210`
    - Swap the `pivot` with the number that is larger from the right
        - `9876[0]432[1]0` -> `9876[1]432[0]0` -> `9876143200`
    - Reverse the numbers of the rightside of the pivot
        - `98761[43200]` -> `98761[00234]` -> `9876100234`
    - Time Complexity 
        - `O(n)`: In worst case, only three scans of the whole array are needed 
    - Space Complexity 
        -  `O(1)`: No extra space is used. In place replacements are done

- [Source code](source/Single.py)
```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """                                         
        # searching from the rightside to find the number that decreases
        # if the decreasing number is found
            # find the smallest number that is bigger than the decreasing number from the rightside
            # swap the positions of the two numbers
        # make the rightside the smallest by reversing all the numbers
```
