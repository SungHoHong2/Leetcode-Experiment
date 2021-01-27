### Employee Free Time
**Greedy**
- [Concepts](images/)
    - sort the whole intervals and apply Greedy 
- [Source code](source/Events.py)
```python
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # create a array that collects the opening and closing time of intervals 
        # sort the array 
        # set a returning array that collects free intervals 
        # set the flag to track number of opening and closing time 
        # set a variable to track the previous time
        # iterate the sorted times 
            # if there is no openings and there was a closing event
                # append the free interval to the returning array 
            # update the number of openend events
            # keep track of the latest time
        # return the free intervals 
        pass
```

**Priority Queue**
- [Concepts](images/)
    - maintain a heap of the next time an employee has to work
    - insert only essential amount of intervals to the heap for faster computation 
- [Source code](source/PriorityQueue.py)
```python
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # set a list to collect free intervals 
        # create a heap with element [start time, employee id, 'th job]
        # get the earliest start time 
        # loop the heap until depleted 
            # get the time, employee id, 'th job from the heap 
            # if the time does not overlap
                # append the interval to the return list 
            # updating the finishing time 
            # if the current employee has a future schedule 
                # push the next schedule to the heap
        # return the free intervals 
        pass
```