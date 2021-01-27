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
- Concepts    
    - Suppose there are `[7,2,5,10,8]` and `2`
    - Start the binary search from a largest and the smallest maximum value
        - `32` is the largest value that the largest subset can have
        - `10` is the largest value that the smallest subset can have  
    - Find the minimum value in this range with which can split into `2` sub-arrays
        1. Find the middle value `mid = (10+32)/2 = 21`
            - can form into `[7,2,5],[10,8]` 
            - valid, record `21`, update `high = mid-1` reducing the range to `[10,20]`
            
        1. Continue with `mid = (10+20)/2 = 15`
            - can form into `[7,2,5],[10],[8]` 
            - invalid, because `3` subsets, update `low = mid+1` increase the range to `[16,20]`            
            
        1. Continue with `mid = (16+20)/2 = 18` 
            - can form into 2 sub arrays `[7,2,5],[10,8]`  
            - valid, record `18` and update `high = mid-1` reducing the range to `[16,17]`
          
        1. Continue with `mid = (16+17)/2 = 16` 
            - can form into 3 sub arrays `[7,2,5],[10],[8]`  
            - invalid, update `left = mid+1` increasing the range to `[17,17]`          
          
        1. Continue with `mid = (17+17)/2 = 17` 
            - can form into 3 sub arrays `[7,2,5],[10],[8]`  
            - invalid, update `left = mid+1` increasing the range to `[18,17]`
         
        1. `[18,17]` breaks the loop and end the smallest maximum subset as `18` 
         
- [Source code](source/binary.py)
```python
class Solution(object):
    def valid(self, nums, m, pivot):
        # set the number of subsets and the current accumulated value
        # iterate the input
            # accumulate the sum
            # if the sum exceeds the pivot 
                # create a subset 
                # start the new accumulated value 
        # return if the number of subsets are acceptable
        pass
    
    def splitArray(self, nums, m):
        # get the smallest and largest possible value with a single subset
        # set the returning value that records the smallest maximum value of the subset        
        # run binary search until smallest and largest value converges
            # get the pivot
            # update the answer and explore the smaller possible values if the number of subsets are valid     
            # explore larger possible values if the the number of subsets are invalid      
        # return the smallest maximum value of the subset 
        pass
```