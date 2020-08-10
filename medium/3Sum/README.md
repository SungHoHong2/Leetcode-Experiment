### 3Sum
**Two Pointers**
- [Source code](source/twoPointers.py)
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # set the return array that contains the elements that sum up to zero
        # assume that the input array is already sorted 
        # iterate the numbers
            # if the current index is above zero  
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

**Hashset**
- [Source code](source/hashset.py)
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # set the return array
        # assume that the array is already sorted
        # iterate the array
            # if the current element is above zero
                # stop the iteration
            # if the element is the first or not duplicated
                # invoke the twoSum function
        # return the result

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        # create a hashset
        # set the index of the leftmost element that is at the rightside of the current element
        # iterate the array
            # calculate the complement
            # if the complement is not in the memory
                # record the current element
            # if the complement is in the hashset
                # skip the leftmost indexes that are duplicates
            # increament the leftmost index
```

**No-Sort**
- [Concepts](images/)
- [Source code](source/)
- [Reference #1]()   