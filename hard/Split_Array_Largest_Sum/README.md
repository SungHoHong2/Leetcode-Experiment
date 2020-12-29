### Split Array Largest Sum
**DP (not accepted)**
- [Concepts](images/dp.png)
- [Source code](source/dp.py)
```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # set the total length of the input
        # set a dp table using columns as the number of subsets and n as the inputs in the array
        # create an array to easily create the potential jth subset
        # set the smallest maximum subset to zero when array is zero
        # expanding the range of the array
            # expanding the number of subsets
                # get the minimum part
                    # smallest maximum sum by comparing the j-1 subsets with potential jth subsets
        # return the smallest maximum subset
        pass
```

**Binary Search + Greedy**
- [Concepts](images/)
    - Suppose `[7,2,5,10,8]` and `2`
    - `max_sum([7,2,5,10,8], 2)` will be in the range `[10, 32]` 
        - `32` is the largest value that a single subset can have
        - `10` is the smallest value that a single subset can have  
    - Find the minimum value in this range with which can form 2 sub-arrays
        1. Start with 10
            - can form into 4 sub arrays `[7, 2],[5],[10],[8]`
            - increase the minimum value to reduce the number into 2 sub arrays
        1. Continue with `mid = (10+32)/2 = 21`
            - can form into 2 sub arrays `[7,2,5],[10,8]` 
            - valid, record `21`, update `high = mid-1` reducing the range to `[10,20]`
            
        1. Continue with `mid = (10+20)/2 = 15`
            - can form into 3 sub arrays `[7,2,5],[10],[8]` 
            - invalid, update `low = mid+1` reducing the range to `[16,20]`            
            
        1. Continue with `mid = (16+20)/2 = 18` 
            - can form into 2 sub arrays `[7,2,5],[10,8]`  
            - record `18` and update `high = mid-1` reducing the range to `[16,17]`
          
        1. Continue with `mid = (16+17)/2 = 16` 
            - can form into 3 sub arrays `[7,2,5],[10],[8]`  
            - invalid, update `left = mid+1` reducing the range to `[17,17]`          
          
        1. Continue with `mid = (17+17)/2 = 17` 
            - can form into 3 sub arrays `[7,2,5],[10],[8]`  
            - invalid, update `left = mid+1` reducing the range to `[18,17]`
         
        1. `[18,17]` breaks the loop and end the smallest maximum subset as `18` 
         
- [Source code](source/binary.py)
```python
class Solution(object):
    def is_valid(self, nums, m, mid):
        # count the number of subsets that has the value within the pivot
        # return true if the number of subsets is valid 
        pass
    
    def splitArray(self, nums, m):
        # set the smallest value of the subset as the low and the largest as the right
        # set the returning value that records the smallest maximum value of the subset        
        # run binary search until low and high coverges
            # get the pivot 
            # update the answer and explore left if the subsets are valid
            # explore right if the the subsets are invalid 
        # return the smallest maximum value of the subset 
        pass
```