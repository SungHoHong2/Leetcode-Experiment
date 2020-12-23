class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # create a array that collects the start and closing time of intervals
        OPEN, CLOSE = 0, 1
        events = []
        for emp in schedule:
            for iv in emp:
                events.append((iv.start, OPEN))
                events.append((iv.end, CLOSE))
        # sort the array
        events.sort()
        # set a returning array that collects free intervals
        ans = []
        # start greedy
        bal = 0
        prev = None
        for t, cmd in events:
            if bal == 0 and prev != None:
                ans.append(Interval(prev, t))

            bal += 1 if cmd is OPEN else -1
            prev = t
        # return the free intervals
        return ans