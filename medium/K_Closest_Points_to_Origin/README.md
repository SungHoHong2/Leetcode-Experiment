### K Closest Points to Origin
**Sort**
- [Source code](source/Sort.py)
```python
class Solution(object):
    def kClosest(self, points, K):
        # sort the array based on the euclidean distance to the original point 
        # return the kth amount of the list
```

**Divide and Conquer**
- quick selecting by a pivot x
    - choose some random element `x = A[i]`
    - split the array into two buckets:
        - one bucket of all the elements less than x,
        - another bucket of all the elements greater than or equal to x
      
- Suppose `work(i, j, K)` of partially sorting the subarray `(points[i], points[i+1], ..., points[j])` 
    - the smallest `K elements` of this subarray occur in the first K positions `(i, i+1, ..., i+K-1)`.
- `quickselect` by a random pivot element from the subarray
    - we have two pointers i and j, and move these pointers to the elements that are in the wrong bucket -- then, we swap these elements.
    - After, we have two buckets `[oi, i]` and `[i+1, oj]`, where `(oi, oj)` are the original `(i, j)` values when calling `work(i, j, K)`
- Say the first bucket has `10 items` and the second bucket has `15 items`.
    - If we were trying to partially sort say, `K = 5` items, then we only need to partially sort the first bucket: `work(oi, i, 5)`. 
    - Otherwise, if we were trying to partially sort say, `K = 17 items`, then the first 10 items are already partially sorted, and we only need to partially sort the next 7 items: `work(i+1, oj, 7)`.


- [Concepts](images/)
- [Source code](source/)
- [Reference #1]()

**Solution3**
- [Concepts](images/)
- [Source code](source/)
- [Reference #1]()