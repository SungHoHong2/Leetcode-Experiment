### Consecutive Numbers Sum
**Count odd factors**
- [Concepts](images/consecutive.png)    
- [Source code](source/consecutive.py)
```python
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        """
        x                       = x+(0+0) 
        x + (x+1)               = 2x+(0+1)
        x + (x+1) + (x+2) ...   = 3x+(1+2) ...
        """
        # return 1 if the input is 1 
        # construct the formula: x+(0+0)=N, 2x+(0+1)=N, 3x+(1+2)=N, ... 
            # create the (prev + curr) == (0+0),(0+1),(1+2) ... 
            # create the div*x == x, 2x, 3x, ...
            # # return the answer when the formula exceeds N
            # # count the number of consecutive numbers if formual equals to N       
```
