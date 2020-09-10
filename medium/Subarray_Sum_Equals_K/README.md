### Subarray Sum Equals K

**Hashmap**
- [Concepts](images/Hashmap.png)
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
