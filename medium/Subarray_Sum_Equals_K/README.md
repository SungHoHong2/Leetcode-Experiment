### Subarray Sum Equals K 

**Hashmap**
- [Concepts](images/Hashmap.png)
    1. Assuming the equation `sum[i]+sum[j]=k` 
        - Suppose there is array that is represented by indexes
            - `sum = [0,1,2,3,4,5,6,7,8,9,10]`
            - `sum[i]=[0,1,2,3,4]`, `sum[j]=[6,7,8,9,10]`
    1. Use the `hashmap` to record the possible results from continuous subsets
        - Suppose that `[0,0,0,0,0]` equals to zero
        - The `hashmap` collects the possible subsets of zero and accumulate them as the results  
            - `1 + 2 + 3 + 4 + 5 = 15`
            - the indexes of the subsets look like `[0]`, `[0,1]`, `[1,0]`, `[0,1,2]`, .... 
    1. Count the number of continuous subsets that equals `k` by finding the `sum[j]` that are equal to `sum[i]-k` 
- [Source code](source/Hashmap.py)
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # initialize a hashmap that records the number of contiguous subsets that sum up to a number
        # set the variables for the number of subsets and the sum of the current subset 
        # record the number of contiguous subsets that sum up to zero
        # iterate the numbers 
            # expand the size of the contiguous subset
            # aggregate the number of contiguous subsets that can be equal to k
            # record the number of the contiguous subsets that equals to a certain number
        # return the number of counts
        pass
```
