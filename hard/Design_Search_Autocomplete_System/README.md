### Design Search Autocomplete System
**Hashmap**
- Concept
    - Apply the `hashmap` that maps the sentence with the frequency 
    - Append the recommendations when the two conditions are met 
        1. the search is part of the sentence 
        1. the search is located at the start of the sentence
    - Sort the recommendations according to the frequency 
- [Source code](source/Hashmap.py)
```python
class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        # set a global hashmap[sentence]=times
        # set a global prefix
        # store the history in the hashmap
        pass

    def input(self, c: str) -> List[str]:
        # if the search ended
            # store the new history to the hashmap
            # reset the prefix
        # if ongoing search
            # accumulate the characters
            # create a return list
            # iterate the hashmap
                # if the accumulated characters are the subset and starts at the beginning of the keys
                    # append to the return list
            # sort the return list by frequency and ascii order
            # return three recommendations
        pass 
```

**Using One level Indexing**
- Concepts
    - One level HashMap
        - The Top level stores the starting character of the sentence as the key
        - The Second level stores the sentence as the key and the frequency as the value
- [Source code](source/OneLevel.py)
```python
class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        # set a global one-level hashmap[sentence[0]] = hashmap[sentence[:]] = int
        # set a global prefix
        # store the history in the hashmap
        pass
            
    def input(self, c: str) -> List[str]:
        # if the search ended
            # store the new sentence to the hashmap 
            # update the frequency of the sentence 
            # reset the global prefix 
        # if ongoing search
            # accumulate the characters
            # create a return list
            # iterate the hashmap
                # if the accumulated characters are the subset and starts at the beginning of the keys
                    # append to the return list
            # sort the return list by frequency and ascii order
            # return three recommendations
        pass
```

**Using Trie**
- [Concepts](images/)
- [Source code](source/Trie.py)
```python
class AutocompleteSystem:
    def __init__(self, sentences, times):
        # create a Trie and store the input 
        # set the global head of the Trie 
        # set global variable of the ongoing search 
        pass

    def createTrie(self, sent, time):
        # create a Trie using characters from input 
        # record the frequency at the finishing sentence 
        pass

    def appendTrie(self, cur):
        # increase the frequency the new or existing sentence in the Trie 
        pass

    def dfs(self, cur, path, ans):
        # explore append all the finishing sentence to the returning list
        pass       

    def input(self, c):
        # if search is finished, add a new sentence in the Trie 
        # accumulate the input 
        # explore deeper or create a new leaf in the Trie 
        # set a list to collect the possible candidates 
        # explore the candidates using dfs 
        # return the at most three best candidates
        pass
```
