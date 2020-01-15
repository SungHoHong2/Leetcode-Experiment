class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        start = sorted(item[0] for item in intervals)
        end = sorted(item[1] for item in intervals)
        ps = 0
        pe = 0
        room = 0

        while ps < len(intervals):

            if start[ps] >= end[pe]:
                room -= 1
                pe += 1

            room += 1
            ps += 1

        return room

