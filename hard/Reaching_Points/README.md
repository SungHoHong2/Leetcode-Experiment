### Problem Title
**Work Backwards**
- [Concepts](images/)
    - Every parent point (x, y) has two children, (x, x+y) and (x+y, y)
    - Every point (x, y) only has one parent candidate 
        - (x-y, y) if x >= y
        - (x, y-x) if x < y 
        - because we never have points with negative coordinates
    - Example 
        - if the target point is (19, 12)
            - the successive parents must have been (7, 12), (7, 5), and (2, 5);
                - (2, 5) is a starting point of (19, 12)
        
- [Source code](source/WorkBackwards.py)
```python
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        # iterate until leaf (tx,ty) reaches or exceeds the root (sx,sy)
            # return true if the leaf meets the root 
            # subtract y from x if x is bigger than y 
            # subtract x from y if y is bigger than x 
        # return false the leaf exceeds the root
        pass
```

**Work Backwards (Modulo Variant)**
- [Concepts](images/)
    - Speed up reaching to the root by bundling together parent operations
        - next parent operations will be to subtract `ty` from `tx` until `tx = tx % ty`
    - if `x > y` and `y` has not reached the root
        - replace `while tx > ty: tx -= ty` with `tx %= ty`
    - if `x > y` and `y` reached the root 
        - only `tx` changes, by subtracting `ty`
        - check whether `ty` can reduce the `tx` to `sx` 
        - `(tx - sx) % ty == 0`
- [Source code](source/Modulo.py)
```python
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):        
        # iterate until leaf (tx,ty) reaches or exceeds the root (sx,sy)
            # stop the search if tx and ty are equal
            # if tx is larger than ty
                # if ty did not reached the root 
                    # subtract tx to the very limit 
                # if ty reached the root 
                    # check whether the ty can reduce tx to sx
            # same operation 
        # return true if tx and ty reached the root
        pass
```