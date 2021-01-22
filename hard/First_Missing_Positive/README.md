### First Missing Positive

**Hashmap**
- Concept
    1. Check if `1` is present in the array 
    2. Apply the hashmap to collect the missing numbers in the array
    3. Return the smallest missing number or create the next larger number
- [Source code](source/Hashmap.py)
```python
class Solution:
    def firstMissingPositive(self, nums):
        # get the largest number possible in the input 
        # return 1 if the input does not contain 1            
        # return 2 if the input only contains 1 
        # create a hashmap that checks the possible numbers 
        # collect the numbers that are not negative numbers, zeros, and numbers larger than n
        # return the missing number if exists   
        # return the n + 1 if all number exists 
        pass
```

**Index as a hash key**
- Concepts
    1. Check if `1` is present in the array 
        - `[3,4,-1,-2,1,5,16,0,2,0]`, `1` does not exist
    2. Data clean up: replace negative numbers, zeros and number larger than `n` by `1`s
        - `[3,4,1,1,1,5,1,1,2,1]`
    3. Walk along the array. Change the sign of the items.
        - Use `index` of the array as a hash key and `number sign` as a presence detector
            - If nums[1] is negative that means that number `1` is present in the array
            - If nums[2] is positive means that number `2` is missing.
                - `[3,4,1,1,1,5,1,1,2,1]`, there is `1,2,3,4,5`
                - `[3,-4,-1,-1,-1,-5,1,1,2,1]`, updated the array `a[1],a[2],a[3],a[4],a[5]`
    4. Return the index of the first positive item
- [Source code](source/InPlace.py)

```python
class Solution:
    def firstMissingPositive(self, nums):
        # get the largest number         
        # return 1 if the input does not contain 1            
        # Suppose that there is 1 in the input return 2 if the length of the input is 1        
        # Replace negative numbers, zeros, and numbers larger than n by 1s (since 1 already exists).          
        # Use index as a hash key and number sign as a presence detector
            # get the value to use as an index (consider that the value is continuously updated)
            # mark the largest number(n) as exist(negative)
            # mark the number between 1 and n as exist(negative)
        # return the missing number(positive) if exists   
        # return n if only the last number is missing 
        # return the n + 1 if all number exists 
        pass
```