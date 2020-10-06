### Group Anagrams
- Given an array of strings `strs`, group the **anagrams** together. 
    - a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
- You can return the answer in any order.
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Categorize by Sorted String**
- [Concepts](images/Sorted.png)
- [Source code](source/Sorted.py)
```python
class Solution(object):
    def groupAnagrams(self, strs):
        # create a map which uses the value as a list
        # iterate the strings
            # save the sorted string as the key and add the string to the list
        # return the grouped values
```

**Categorize by Count**
- [Source code](source/)
```python
class Solution:
    def groupAnagrams(strs):
        # create a map that uses values as a list
        # iterate the string
            # create a array of alphebatical order
            # iterate the string
                # count the number of each character
            # store the number of the count as the key and append the string as a value
        # return the result
```