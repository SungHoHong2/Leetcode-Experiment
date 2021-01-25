### Edit Distance

**Dynamic Programming**
- [Concepts](images/dp.png)
    - an edit distance `D[i][j]`
        - the first `i` characters of `word1`
        - the first `j` characters of `word2`
        - can compute knowing `D[i - 1][j]`, `D[i][j - 1]` and `D[i - 1][j - 1]`
            - just one more character to add into one or both strings 
    - If the last character is the same `word1[i] = word2[j]`
        - `D[i][j] = 1 + min( D[i-1][j], D[i][j-1], D[i-1][j-1]-1 )`
            - `D[i-1][j]`: change 1 from word1 to become `word1[i] = word2[j]` 
            - `D[i][j-1]`: change 1 from word2 to become `word1[i] = word2[j]`  
            - `D[i-1][j-1]`: no need to change anything 
    - If the last character is not same `word1[i] != word2[j]`
        - `D[i][j] = 1 + min( D[i-1][j], D[i][j-1], D[i-1][j-1] )`
            - `D[i-1][j-1]`: change either word1 or word2 to become `word1[i] = word2[j]` 
- [Source code](source/dp.py)

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # get the length of the word1
        # get the length of the word2 
        # return the total length of a word if one of the word is empty
        # set a dp table
        # update the number of changes for word1
        # update the number of changes for word2
        # iterate the dp for word1  
            # iterate the dp for word2
                # case1: get the minimum number of changes for word1 to become word2
                # case2: get the minimum number of changes for word2 to become word1
                # case3: get the minimum number of changes for before word1 and word2 changes   
                # increase the number of changes for case3 if word1 and word2 are not equal
                # update the minimum number of changes for word1 and word2 become equal 
        # return the minimum number of changes
        pass
```