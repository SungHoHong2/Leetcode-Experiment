### Subarray Sum Equals K
**Hashmap**
- [Concepts](images/Hashmap.png)
    1. Follows the concept of dynamic programming
    1. Assuming the equation `sum[i]−sum[j]=k` 
        - Find the number of possible `sum[j]` from `sum[i]-k=sum[j]` 
    1. Use the `hashmap` to record the total number of possible subsets for creating every possible `sum[i]` 
    1. Count the number of subsets by finding the `sum[j]` that are equal to `sum[i]-k` 

- [Source code](source/Hashmap.py)
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # initialize a hashmap 
        # set the variables for counter and the sum 
        # count zero in hashmap 
        # iterate the numbers 
            # accumulate the sum 
            # if the sum subtracted from k is found in hashmap
                # subarray sum of k exists so increase the number of counts
            # if the sum is found again in the hashmap  
                # increase the number of counts 
            # if the sum does not exist in the hashmap 
                # start counting the sum in hashmap 
        # return the number of counts
```
