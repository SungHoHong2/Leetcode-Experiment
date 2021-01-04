### Subarray Sum Equals K 

**Hashmap**
- [Concepts](images/Hashmap.png)
    1. Assuming the equation `sum[i]+sum[j]=k` 
    1. Use the `hashmap` to record the possible results from continuous subsets
    1. Count the number of continuous subsets that equals `k` by finding the `sum[j]` that are equal to `sum[i]-k` 
- [Source code](source/Hashmap.py)
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # initialize a hashmap that records the number of contiguous subsets that sum up to a number
        # set the variables for counter and the sum 
        # record the number of contiguous subsets that sum up to zero
        # iterate the numbers 
            # expand the size of the contiguous subset
            # if the contiguous subset that sums up to k is found
                # aggregate the number of subsets that can be equal to k
            # record the number of the contiguous subsets that equals to a certain number
        # return the number of counts
        pass
```
