### 4Sum II
**Hashmap**
- [Concepts](images/)
- [Source code](source/Hashmap.py)
```python
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # set a return variable that records the number possible solutions
        # create a table that records the complements
        # iterate both list A and B
                # record the number of all possible sum
        # iterate both list C and D
                # accumulate the number of possible sum that equals to zero
        # return the possible numbers
        pass
```

**kSum II**
- [Concepts](images/)
    - divide k arrays into two groups
        - the first group counts the sums of the k/2 arrays 
        - the second group, search for complements of the first group
- [Source code](source/kSum.py)
```python
  
class Solution:
    def addToHash(self, lists, m, i, sum):
        # record the sum if the array reaches the second half 
        # accumulate if the array is within the first half
        pass

    def countComplements(self, lists, m, i, complement):
        # return the counts if the sum matches the complement
        # set the counter to record the answer 
        # accumulate the second half of the array and count the results that reaches the complement
        # return the total number of counts 
        pass
    
    def nSumCount(self, lists):
        # create a table that records the complements
        # sum up the the first half and store them as complements in the hashtable 
        # check if the sum reaches zero by comparing the complements of the first with the second half
        pass
    
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # introduce an algorithm that allows n arrays
        pass
```