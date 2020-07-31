### Valid Palindrome
**Compare with Reverse**
- [source code](source/reverse.py)
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert the argument into a lower letter containing only characters or numbers
        # compare the resulting array with the reversed array
```

**Two Pointers**
- [source code](source/twoPointer.py)
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set the two pointers for the start and the end
        # loop until the two pointers converge
            # if the two pointers did not converge and the start is not a number or character
                # skip
            # if the two pointers did not converge and the end is not a number or character
                # skip
            # if the start and the end are not identical
                # return false
            # decrease the distance between start and end
        # if no problem detected then it is a palindrome
```
