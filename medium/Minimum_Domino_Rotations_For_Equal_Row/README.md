### Minimum Domino Rotations For Equal Row
**Greedy**
- [Source code](source/Greedy.py)
```python
class Solution:
    def check(self, A, B, target):
        # set up the variable for rotations made by A and. B
        # iterate the dominos
            # if both A and B are different from the target
                # return false
            # if A is wrong
                # rotate A
            # if B is wrong
                # rotate B
        # return the minimum number of rotations
        pass
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # invoke the check function and get the minimum number of rotations
        # if the rotation value is valid
            # return the minimum number of rotations
        # if the rotation does not provide any value
            # get the return value from B
        pass
```

**Counting with hashmap**
- [Source code](source/Counting.py)
```python
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # create a map counting the number of hits for A
        # create a map counting the number of hits for B
        # create a map counting the number of hits for both A and B
        # iterate the dominos
            # count the number of hits for A
            # count the number of hits for B
            # if both A and B are equal
                # count the number of hits for both A and B
        # iterate through the map
            # if the hits from A and B - (both) equals the total number of dominos
                # return the shortest possible result
        # if cannot find return false
        pass
```


