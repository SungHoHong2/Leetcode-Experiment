### Longest Palindromic Substring

**Expand Around Center**
- [Concepts](images/expand.png)
- [Source code(1)](source/brute.py)
- [Source code(2)](source/expand.py)
- Time complexity : **O(n^2)**
- Space complexity : **O(1)**

```python
class Solution:
    # function for checking the largest palindrome
    def palindrome(self, arr, index):
        # set the variables for the odd palindrome
        # loop until the palindrome is invalid 
            # increase the size of the odd paliindrome
            # increase the left and right index          
        # set the variables for the even palindrome
        # loop until the palindrome is invalid       
        # return the largest odd or even palindrome
        
    def longestPalindrome(self, s: str) -> str:
        # set the variable for the largest substring 
        # if the string is less than equal to one
            # return the original input 
        # iterate the string
            # invoke palindrome checker and get the left and right index 
            # if the length of the substring creates a new record
                # update the largest substring
        # return the largest substring        
```

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # initialize the start and the end
        # iterate the string
            # in case the total length is odd
            # in case the total length is even
            # get the longest maxLength
            # if the maxlength hits the record
                # update the start and end variable
        # after divided return the substring result
    # function that returns the largest length of the palindrome
        # set up the pointers for left and right
        # expand until it there is no palindrome
        # return the length of the palindrome
```

**Dynamic Programming**
- [Concepts(1)](images/dynamic.png)
- [Concepts(2)](images/dynamic2.png)
- [Source code](source/dynamic.py)
- [Reference](https://www.youtube.com/watch?v=UflHuQj6MVA&t=359s)
- Time complexity : **O(n^2)**
- Space complexity : **O(n^2)**

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # construct the matrix of dp
        #     b  a  b  a  d
        #  b [0, 0, 0, 0, 0]
        #  a [0, 0, 0, 0, 0]
        #  b [0, 0, 0, 0, 0]
        #  a [0, 0, 0, 0, 0]
        #  b [0, 0, 0, 0, 0]
        # create the table
        # set the start variable
        # set the maximum length of the palindrome
        # check the palindrome of a single character
        # check the palindrome of a neighboring character
        # check the palindrome that has the size from 3 to n
            # starting point of the substring (make sure n-k != 0)
                # end point of substring (make sure k < len(s))
                # if cells from i and j are equal and the history is true
        # return the result
```