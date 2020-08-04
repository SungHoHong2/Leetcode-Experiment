### Longest Palindromic Substring

**Brute Force**
- [source code](source/brute.py)
```python
class Solution:
    # function for checking the largest palindrome
        # set the left and right index for the odd palindrome
        # set the variable for the largest odd palindrome
        # loop until left and right reach the end 
            # if it is a plaindrome 
                # increase the size of the odd paliindrome
            # if it is not a palindrome 
                # escape the loop
            # increase the left and right index 
        # left and right index for the even palindrome
        # find the even palindrome using the same method of finding the odd palindrome 
        # if odd palindrome is larger 
            # return the index for the odd palindrome 
        # if even palindrome is larger 
            # return the index for the even palindrome and note that even has no centerpoint 

    def longestPalindrome(self, s: str) -> str:
        # set the variable for the largest substring 
        # if the string is none
            # return empty string 
        # if the string length is only one 
            # return the string
        # iterate the string
            # invoke palindrome checker and get the left and right index 
            # if the length of the substring creates a new record
                # update the largest substring
        # return the largest substring
```


**Dynamic Programming**
- [concepts](images/dynamic.png)
- [source code](source/dynamic.py)

**Expand Around Center**
- [concepts](images/expand.png)
- [source code](source/expand.py)
