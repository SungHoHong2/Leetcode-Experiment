from heapq import heappush
from heapq import heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # return zero if there are not scheduled meetings
        if not intervals:
            return 0
        # Initate a heap to keep track of the earliest finish time
        free_rooms = list()
        # Sort the meetings in an ascending order according to the start time
        intervals.sort()
        # Push the finish time of the first meeting to the heap using heapq.heapush(list, value)
        heappush(free_rooms, intervals[0][1])
        # Iterate all the remaining meetings
        for interval in intervals[1:]:
            # if the earliest finish time is smaller than the current meeting
            if free_rooms[0] <= interval[0]:
                # empty the finished meeting and add the current meeting
                heappop(free_rooms)
            # add the finish time of the current meeting to the heap
            heappush(free_rooms, interval[1])
        # return the size of the heap
        return len(free_rooms)