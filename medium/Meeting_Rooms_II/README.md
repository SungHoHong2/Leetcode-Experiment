### Meeting Rooms II
**Priority Queues**
- Concepts
    1. Sort the meetings according to start time 
    2. Use the priority queue to store the non overlapping meetings
    3. Use the priority queue to return the earliest finish time of the valid meetings
- [Source code](source/Priority.py)
```python
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # if there are not scheduled meetings
            # return zero
        # Initate a heap to keep track of the earliest finish time
        # Sort the meetings in an ascending order according to the start time.
        # Push the finish time of the first meeting to the heap using heapq.heapush(list, value)
        # Iterate all the remaining meetings
            # if the earliest finish time is smaller than the current meeting
                # empty the finished meeting and add the current meeting
            # add the finish time of the current meeting to the heap
        # return the size of the heap
        pass
```

**Chronological Ordering**
- Concepts 
    1. Create two arrays sorted by start and finish time 
    1. Give rooms for all the meeting rooms that are sorted by start time  
    1. Reduce the meeting rooms by checking the rooms of the finish time
- [Source code](source/Chronological.py)
````python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # If there are no more scheduled meetings
            # return zero
        # set a variable to keep track of used rooms
        # Sort the start time of the meetings
        # Sort the finish time of the meetings
        # Set the pointer for start and finish time array
        # Iterate all the meetings using the start pointer
            # If there is a meeting tht does not overlap
                # reduce the number used rooms
                # increment the pointer for the finish time
            # increase the number of used room
        # return the number of used rooms
        pass
````
