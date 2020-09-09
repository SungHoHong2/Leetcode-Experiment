import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # if there are not scheduled meetings
        if not intervals:
            # return zero
            return 0
        # Initate a heap to keep track of the earliest finish time
        free_rooms = []
        # Sort the meetings in an ascending order according to the start time.
        intervals.sort()
        # Push the finish time of the first meeting to the heap using heapq.heapush(list, value)
        heapq.heappush(free_rooms, intervals[0][1])
        # Iterate all the remaining meetings
        for i in intervals[1:]:
            # if the earliest finish time is smaller than the current meeting
            if free_rooms[0] <= i[0]:
                # empty the finished meeting and add the current meeting
                heapq.heappop(free_rooms)
            # add the finish time of the current meeting to the heap
            heapq.heappush(free_rooms, i[1])
        # return the size of the heap
        return len(free_rooms)