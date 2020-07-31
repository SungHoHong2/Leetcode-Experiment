### Problem Title
**Naive Approach**
- [source code](source/naive.py)
```python
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # set the return array
        # iterate through the nums
            # check whether the current number is divisible by 3
            # check whether the current number is divisible by 5
            # Divides by both 3 and 5, add FizzBuzz
            # Divides by 3, add Fizz
            # Divides by 5, add Buzz
            # Not divisible by 3 or 5, add the number
        # return array
```

**Hashmap**
- [source code](source/hashmap.py)
```python
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # set the return array
        # set a hashmap to store all fizzbuzz mappings
        # iterate the numbers
            # set a temp string
            # iterate the available keys in the hashmap
                # If the num is divisible by key,
                    # then add the corresponding string mapping to current num_ans_str
            # if there is no divisible nums
                # add the num
            # Append the current answer str to the ans list
        # return the array
```
