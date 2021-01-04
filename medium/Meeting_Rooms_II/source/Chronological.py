class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Return zero if there are no more scheduled meetings
        if not intervals:
            return 0
        # Set a variable to keep track of used rooms
        used_rooms = 0
        # Sort the start time of the meetings
        starts = sorted([i[0] for i in intervals])
        # Sort the finish time of the meetings
        ends = sorted(i[1] for i in intervals)
        # Set the pointer for start and finish time array
        end = 0
        # Iterate all the meetings using the start pointer
        for start in range(len(intervals)):
            # If there is a meeting tht does not overlap
            if starts[start] >= ends[end]:
                # reduce the number used rooms
                used_rooms -= 1
                # increment the pointer for the finish time
                end += 1
            # increase the number of used room
            used_rooms += 1
        # return the number of used rooms
        return used_rooms

