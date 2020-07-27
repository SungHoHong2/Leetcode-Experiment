### Reorder Data in Log Files
**Custom Sort**
- [source code](source/sort.py)

```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # define custom sorting 
            # split log into id and the log
            # if the log contains string 
                # give higher priority based on 1) string, 2) lexographical order of the log, order of the id
            # if the log contains digit
                # give less priority 
        # run the sorted function with the custom sorting
```
