### Before and After Puzzle
**Using Sets**
- Concepts
    - Create a map that stores the first string as the key and the rest of the strings as the value 
        - `writing code` = `first["writing"] = {"code"}`
    - Create a map that stores the last string as the key and the rest of the strings as the value 
        - `writing code` = `first["code"] = {"writing"}`
    - Merge all of the possible overlaps using the two maps
- [Source code v1](source/UsingSets.py)
- [Source code v2](source/UsingSets2.py)

```python
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        # create the map that stores the first string of the phrases as the key and the rest as a set
        # create the map that stores the last string of the phrases as the key and the rest as a set
        # create the return set
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