### Minimum Domino Rotations For Equal Row
**Greedy**
- [Source code](source/Greedy.py)
```python
class Solution:
    def check(self, x, n):
        # set up the variable for rotations made by A and. B
        # iterate the dominos
            # if both A and B are different from the target
                # return false
            # if A is wrong
                # rotate A
            # if B is wrong
                # rotate B
        # return the minimum number of rotations
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # invoke the check function and get the minimum number of rotations
        # if the rotation value is valid or A and B have the same value
            # return the minimun numvber of rotations
        # if the rotation does not provide any value
            # get the return value from B
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
```

**Counting top and bottom**
- [Source code](source/TopBottom.py)
```python
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # iterate two candidate from A and B
            # set the variable for counting the top and the bottom
            # iterate the dominos
                # if the candidate is not part of A or B then break
                # if candidate is not found in B
                    # count the bottom
                # if the candidate is not found in A
                    # count the top
            # if the no break after iterating the dominos
                # return the minimum number of rotations
        # return the -1
```

**Intersection**
- [Source code](source/Intersection.py)
```python 
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # combine elements of A, B together as a set
        print([set(d) for d in zip(A, B)])
        # get the common value checking the combined sets        
        s = functools.reduce(operator.and_, (set(d) for d in zip(A, B))) 
        # if there is no common value 
        if not s: 
            # return false 
            return -1
        # if there is a common value 
        x = s.pop()
        # return the minimum number of swaps
        return min(len(A) - A.count(x), len(B) - B.count(x))
```



