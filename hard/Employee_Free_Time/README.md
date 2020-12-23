### Employee Free Time
**Greedy**
- [Concepts](images/)
    - sort the whole intervals and apply Greedy 
- [Source code](source/Events.py)
```python
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # create a array that collects the start and closing time of intervals 
        # sort the array 
        # set a returning array that collects free intervals 
        # start greedy
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