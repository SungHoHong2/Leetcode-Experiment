### Before and After Puzzle
**Using Sets**
- [Source code](source/UsingSets.py)
```python
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        # create the map that stores the first string of the phrases as the key and the rest as a set
        # create the map that stores the last string of the phrases as the key and the rest as a set
        # create the return set
        # x = {"a", "b", "c"}
        # y = {"c", "e", "f"}
        # x |= y
        # x = {'a', 'b', 'c', 'e', 'f'}
        # iterate the phrases
            # split the phrase into an array of string by space
            # if the first string of the current phrase matches with some last string of the other phrase
                # combine the overlapping phrases {rest of the last string + last string}
            # if the last string of the current phrase matches with the first string of the other phrase
                # combine the overlapping phrases {first string + rest of the first string}
            # store the first string as the key and the rest in a set
            # store the last string as the key and the rest in a set
        # return with the sorted result
        pass
```