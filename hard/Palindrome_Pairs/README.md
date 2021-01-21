### Palindrome Pairs
**Hashmap**
- Concepts
    - Case1: A palindrome pair is formed by 2 words that are the reverse of each other.
    - Case2: The first word is shorter than the second word. 
        - The second word starts with a palindrome, and ends with the reverse of the first word.
    - Case3: The first word is longer than the second word.
        - The first word ends with a palindrome, and starts with the reverse of the second word.
       
    ![hashmap](images/Hashmap.png)
- [Source code](source/Hashmap.py)
```python
class Solution:
    def validSuffixes(self, word):
        # set the array that collects word2 substring comparable to word1
        # iterate the word2
            # append the rightside to the array if the leftside is a palindrome
        # return the substrings that can be compared with word1
        pass
    
    def validPrefixes(self, word):
        # set the array that collects word1 substring comparable to word2
        # iterate the word1
            # append the leftside to the array if the rightside is a palindrome
        # return the substrings that can be compared with word2
        pass

    def palindromePairs(self, words):
        # set the hashmap[word] = index
        # set the array to store the possible pairs
        # iterate the input
            # get the reversed word
            # case1: both words are palindrome to each other                    
            # case2: if word1 is shorter than word2         
            # case3: if word1 is longer than word2        
        # return the available pairs
        pass
```

**Trie**
- [Source code](source/Trie.py)
```python
class TrieNode:
    def __init__(self):
        # set the pointer to the next level
        # set the indicator that the current level is a finished word
        # set the indicator that the current level is a palindrome
        pass

class Solution:
    def palindromePairs(self, words):
        # Create the Trie
        # add the reversed nodes in the Trie
                # Label the the remainder if they are a palindrome.
            # mark the current level with the current word

        # Look up each word in the Trie and find palindrome pairs.
            # case 3: if word1 is longer than word2
                # if a matching word is found in the current level
                    # check the right side of word1 is a palindrome
                        # add as a solution
                # break if no matching word is found
                # go down to the deeper level of Trie
            # if case 3 is not applied after iterating teh whole word
                # case 1: a palindrome is found
                # case 2: if word2 is longer than word1 and word2 consists a palindrome
        # return the palindrome pairs
        pass
```
