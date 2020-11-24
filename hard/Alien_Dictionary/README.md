### Alien Dictionary

**[General Approach](images/General.png)**
1. Extracting dependency rules from the input.
    -  `A must be before C`, `X must be before D`, or `E must be before B`
2. Putting the dependency rules into a graph with letters as nodes and dependencies as edges
3. Topologically sorting the graph nodes

**Breadth-First Search**
- [Concepts](images/)
    - Identify which letters have no incoming links left
        - Count the number of incoming links for each node
    - Maintain a queue for BFS by starting with the nodes with zero incoming links
- [Source code](source/BFS.py)

**DFS**
- [Concepts](images/)
    - Do not need to count the incoming links 
    - Detect cycles by using graph coloring 
- [Source code](source/DFS.py)