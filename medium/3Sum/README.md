### 3Sum
**Two Pointers**
- [Source code](source/twoPointers.py)
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # set the return array that contains the elements that sum up to zero
        # assume that the input array is already sorted 
        # iterate the numbers
            # if the input cannot produce zero  
                # finish iteration 
            # if the first element or the neighboring element is not the same 
                # invoke the twoPointer function
        # return the answers
    
    def twoSum2(self, nums: List[int], i: int, res: List[List[int]]):
        # get the 3 indexes (current, leftmost from the current, and the rightmost indexes) 
        # loop until the indexes converge 
            # calculate the sum
            # if the sum is below zero 
                # increase the leftmost index 
            # if the sum is above zero 
                # decrease the rightmost index 
            # if the sum equals to zero 
                # add the answers to the return array 
                # reduce the range of the left and the right index 
                # loop until left element is not a duplicate of the previous element
```

**Solution2**
- [Concepts](images/)
- [Source code](source/)
- [Reference #1]() 

**Solution3**
- [Concepts](images/)
- [Source code](source/)
- [Reference #1]()   