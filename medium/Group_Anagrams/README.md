### Group Anagrams

**Categorize by Sorted String**
- [Concepts](images/Sorted.png)
    - Sort the characters of the each strings in ascending order 
    - Apply the sorted strings as the key of the hashmap 
    - Group all the strings that share the same table using the hashmap 
- [Source code](source/Sorted.py)
```python
class Solution(object):
    def groupAnagrams(self, strs):
        # create a map which uses the value as a list
        # iterate the strings
            # save the sorted string as the key and add the string to the list
        # return the grouped values
        pass
```

**Categorize by Count**
- Concepts 
    - Avoid sorting the strings
    - Create a one-dimension table that count the number of alphabets included in each string 
    - Group all the strings that share the same table using the hashmap 
- [Source code](source/Count.py)
```python
class Solution:
    def groupAnagrams(self, strs):
        # create a map that uses values as a list
        # iterate the string
            # create a array of alphabetical order
            # iterate the string
                # count the number of each character
            # store the number of the count as the key and append the string as a value
        # return the result
        pass
```