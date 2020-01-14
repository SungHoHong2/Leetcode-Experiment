class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[-1])

        room = []
        heapq.heappush(room, intervals[0][-1])

        for i in range(1, len(intervals)):
            if room[0] <= intervals[i][0]:
                heapq.heappop(room)

            heapq.heappush(room, intervals[i][-1])

        return len(room)