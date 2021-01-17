### Trapping Rain Water
**Brute force**
- [Source code](source/Brute.py)
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        y-axis         #
                   #   ## #
                 # ## ######
                    x-axis
        """
        # initialize the answer variable
        # iterate the list
            # set up the flags for checking maximum left and right
            # find the biggest height of the leftside of the list
            # find the biggest height of the right of the list
            # calculate the current area that can trap the water
            # accumulate the answer
        # return the answer
        pass
```

**Dynamic Programming**
- [Concepts](images/dp.png)
- [Source code](source/Dp.py)
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        # return zero if there is no input 
        # set the table for the maximum height of left and right 
        # record the maximum height from the left 
        # record the maximum height from the right 
        # accumulate the available space for each of the x-axis
        # return the total available space for the rain water
        pass
```

**Using stacks**
- [Concepts](images/stack.png)
- [Source code](source/Stack.py)
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        # set the answer
        # set the stack
        # iterate the heights
            # loop the stack until a hole is detected
                # pop the height that serves as the bottom from the stack 
                # finish the loop if there are no more left heights to compute area  
                # calculate the distance
                # get the left height from the stack
                # get the right height 
                # calculate the available height 
                # aggregate the available space for the rain
            # append the previous heights in the stack
        # return the available space fore the rain
        pass
```

**Using two pointers**
- [Source code](source/TwoPointers.py)
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        # set the pointers for left and right
        # store the record for the largest available space for the rain
        # store the record for the largest left and right
        # loop until left and right converges
            # if right is higher
                # record the largest left if left is going up
                # aggregate the available space if the left is going down
                # move left to right
            # if the left is higher
                # record the largest right if right is going up
                # aggregate the available space if the right is going down
                # move right to left
        # return the accumulated area
        pass
```



