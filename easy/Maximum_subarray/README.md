### Maximum Subarray

**Divide & Conquer**
- [source code](source/divide.py)

```python
class Solution(object):
    
    # define crosssum function  
    def crosssum(self, nums, left, right, mid):
        # if the subarray has a single item        
            # return the item
        # get the largest sum from middle to left
        # get the largest sum from middle to right
        # return the sum of both left and right

    # define recursive function
    def helper(self, nums, left, right):
        # if the subarray is a single item
            # return the number
        # split the subarray into half
        # run the recursive function from left to middle
        # run the recursive function from middle to right
        # check the sum of the subarray starting from the middle
        # return the biggest sum from the three subarrays

    def maxSubArray(self, nums):
        # invoke the recursive function
```

**Dynamic Programming**
- [source code](source/dynamic.py)
```python
class Solution(object):
    def maxSubArray(self, nums):
        # set the current sum and the maxsum to the first element
        # iterate through the numbers
            # record the current sum of the subarray
            # record the maximum sum of the subarray
        # return the maximum sum
```

**Greedy Algorithm**
- [source code](source/greedy.py)

```python
class Solution(object):
    def maxSubArray(self, nums):
        # set up the maximum sum as the first item
        # iterate the numbers
            # if the number is bigger than zero
                # add the current number with the previous number
            # record the maximum sum
        # return the maximum sum
```

