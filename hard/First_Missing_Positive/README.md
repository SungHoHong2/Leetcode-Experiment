### First Missing Positive
**Index as a hash key**
- Concepts
    1. Check if `1` is present in the array 
    2. Data clean up: replace negative numbers, zeros and number larger than `n` by `1`s 
    3. Walk along the array. Change the sign of the items.
        - Use index as a hash key and number sign as a presence detector
            - If nums[1] is negative that means that number `1` is present in the array
            - If nums[2] is positive means that number `2` is missing.
    4. Return the index of the first positive item
    
- [Source code](source/Hashmap.py)
```python
class Solution:
    def firstMissingPositive(self, nums):
        # get the length of the input         
        # return 1 if the input does not contain 1        
        # Suppose that there is 1 in the input return 2 if the length of the input is 1          
        # Replace negative numbers, zeros, and numbers larger than n by 1s (since 1 already exists).
        # Use index as a hash key and number sign as a presence detector.
            # get the value to use as an index
            # update the value of the first index (knowing that 0 no longer exist) if the index equals to n
            # update the value of the index            
        # return the first positive number found in the value of the index         
        # return n if the first index is positive
        # return the n + 1 if all number from 1 to n exists in the input 
        pass
```