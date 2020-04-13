### Breadth First Search

---
**Breadth first search**
1. Find all the possible generic/intermediate states. `ex) hit = *it, h*t, hi*`
2. Push a tuple containing the beginWord and 1 in a `queue`. 
    - The 1 represents the level number of a node.
3. To prevent cycles, use a visited dictionary.  
4. Each word in the `queue` appends `(word, level+1)`
5. If you reach the desired word, its level would represent the shortest transformation.  
 
---
**Bi-directional breadth search**
- We can considerably cut down the search space of the standard breadth first search algorithm if we launch two simultaneous BFS
- One from the beginWord and one from the endWord.
- We progress one node at a time from both sides and at any point in time if we find a common node in both the searches, we stop the search.
- This is known as bidirectional BFS and it considerably cuts down on the search space and hence reduces the time and space complexity.

