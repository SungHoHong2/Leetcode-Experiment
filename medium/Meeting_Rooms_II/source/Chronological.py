class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # If there are no more scheduled meetings
        if not intervals:
            # return zero
            return 0
        # set a variable to keep track of used rooms
        used_rooms = 0
        # Sort the start time of the meetings
        start_timings = sorted([i[0] for i in intervals])
        # Sort the finish time of the meetings
        end_timings = sorted(i[1] for i in intervals)
        # Set the pointer for start and finish time array
        end_pointer = 0
        start_pointer = 0
        # Iterate all the meetings using the start pointer
        for start_pointer in range(len(intervals)):
            # If there is a meeting tht does not overlap
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # reduce the number used rooms
                used_rooms -= 1
                # increment the pointer for the finish time
                end_pointer += 1
            # increase the number of used room
            used_rooms += 1
        # return the number of used rooms
        return used_rooms

