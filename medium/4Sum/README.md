### 4Sum
**Two Pointers**
- Concepts
    - Assume that all the numbers are sorted in the ascending order
    - Recursively reduce the fourSum problem into twoSum problem 
- [Source code](source/TwoPointers.py)
```python
class Solution:
    
    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        # set a list that stores the group of four integers that sums up to the target
        # return the empty list if there is no more input
        # return empty list if smallest or largest possible sum does not cannot reach the target
        # return the result from the twoSum if 2 numbers need to match the target
        # iterate the index
            # if it is the first index or not duplicated
                # append the current number with the the recursion using reduced target and k 
        # return the collection of answers 
        pass    
    
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        # set a return list
        # set a left and right
        # loop until left and right converge
            # compute the sum of left and right
            # move left to right if the sum is smaller than the target
            # move right to left if the sum is bigger than the target
            # append the answer if the sum is equal
            # skip the duplicated inputs
        # return the collection of answers
        pass    
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort the input in ascending order
        # invoke the recursion
        pass
```

**Hash Set**
- Concepts
    - Previously the 3Sum solved the problem without sorting the array
        - need to sort values within triplets
        - doing the same for k values could be impractical
    - Assume that all the numbers are sorted in the ascending order
    - Apply the same recursive technique
- [Source code](source/HashSet.py)
```python
class Solution:
    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        # set a list that stores the group of four integers that sums up to the target
        # return the empty list if there is no more input
        # return empty list if smallest or largest possible sum does not cannot reach the target
        # return the result from the twoSum if 2 numbers need to match the target
        # iterate the index
            # if it is the first index or not duplicated
                # append the current number with the the recursion using reduced target and k
        # return the collection of answers
        pass
    
    def twoSum(self, nums, target):
        # set a return array 
        # create a hashset
        # set the index of the leftmost element that is at the rightside of the current element
        # loop until the indexes converge
            # calculate the complement
            # if the complement is not in the memory
                # record the current element
                # increase the leftmost index
            # if the complement is in the memory
                # add the answer to the return list
                # increase the leftmost index
                # skip the leftmost indexes that are duplicates
        # return an array
        pass
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort the input in ascending order
        # invoke the recursion
        pass
```