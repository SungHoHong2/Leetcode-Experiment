### Consecutive Numbers Sum
**Count odd factors**
- [Concepts](images/consecutive.png)    
- [Source code](source/consecutive.py)
```python
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # return 1 if the input is 1 
        # x + (x+1) + (x+2) + ...  = N 
            # x+(0+0)=N, 2x+(0+1)=N, 3x+(1+2)=N, ... 
            # (x)=N, (2x)+1=N, (3x)+3=N
            # get the result from the division 
            # return the total count if quotient becomes zero  
            # if N is fully divided count the possible numbers 
        pass
```
