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
        events = list()
        for emp in schedule:
            for event in emp:
                events.append((event.start, 'OPEN'))
                events.append((event.end, 'CLOSE'))
        # sort the array
        events.sort()
        # set a returning array that collects free intervals
        ans = list()
        # set the flag to track number of opening and closing time
        bal = 0
        # set first the starting time as previous time
        prev = events[0][0]
        # iterate the sorted times
        for curr, cmd in events:
            # if there is no openings and there was a closing event
            if bal == 0 and prev < curr:
                # append the free interval to the returning array
                ans.append(Interval(prev, curr))
            # update the number of opening events
            bal += 1 if cmd == "OPEN" else -1
            # set the current time as previous
            prev = curr
        # return the free intervals
        return ans