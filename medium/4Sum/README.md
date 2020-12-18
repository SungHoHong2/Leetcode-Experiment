### 4Sum
**Two Pointers**
- [Concepts](images/)
- [Source code](source/)
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            # set a list that stores the group of four integers that sums up to the target
            # return the empty list if there is no more input
            # return empty list if the k number of smallest or largest values cannot match the target
            # return the result from the twoSum if 2 numbers need to match the target
            # iterate the index
                # if it is the first index or not duplicated
                    # append the current number with the the recursion using reduced target and k number
            # return the collection of answers 
            pass

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
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

        # sort the input in ascending order
        # invoke the recursion
        pass
```

**Hash Set**
- [Concepts](images/)
- [Source code](source/)
- [Reference #1]()