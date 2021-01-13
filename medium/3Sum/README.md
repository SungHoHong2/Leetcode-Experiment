### 3Sum
**Two Pointers**
- Concepts 
    - Sort the numbers in ascending order 
    - Only need to search before the positive number
        - Each search expands from center to find the three integers that sum up to zero 
- [Source code](source/twoPointers.py)
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # set the return array that contains the elements that sum up to zero
        # assume that the input array is already sorted 
        # iterate the numbers
            # if the twoSum2 cannot produce zero anymore 
                # finish iteration 
            # if the first element or the neighboring element is not the same 
                # invoke the twoPointer function
        # return the answers
        pass
    
    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
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
        pass
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
        pass

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        # create a hashset for complements
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
        pass
```

**No-Sort**
- Concept 
    - No sorting means, the algorithm cannot handle the duplicates
- [Source code(3)](source/noSort_3.py)
- [Source code(2)](source/noSort_2.py)
- [Source code](source/noSort.py)
```python
class Solution:
    def twoSum(self, nums, i, target, res):
        # create a hashset for complements
        # iterate from left to right
            # calculate the complement
            # if the complement is in the hashset
                # add the results(fix the orders because the answer may append duplicates)
            # record the complement if the complement is not in the hashset
        pass

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create sets for return value and checking for duplicates
        # iterate the each number and run twoSum function 
            # run twoSum only on non duplicates
                # record the duplicates in the set
                # invoke the twoSum function 
        # return the collections that sum up to zero 
        pass
```