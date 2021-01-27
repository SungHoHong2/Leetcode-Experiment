from heapq import heappop, heappush, heapify
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # set a list to collect free intervals
        ans = list()
        # create a list of double end queue that stores the schedule
        events = [collections.deque(emp) for emp in schedule]
        # create a heap with element [start time, employee id]
        pq = [(emp[0].start, i) for i, emp in enumerate(schedule)]
        heapify(pq)
        # get the earliest start time
        prev = pq[0][0]
        # loop the heap until depleted
        while pq:
            # get the time, employee id, 'th job from the heap
            curr, e_id = heappop(pq)
            # if the time does not overlap
            if prev < curr:
                # append the interval to the return list
                ans.append(Interval(prev, curr))
            # updating the finishing time
            prev = max(prev, events[e_id].popleft().end)
            # if the current employee has a future schedule
            if events[e_id]:
                # push the next schedule to the heap
                heappush(pq, (events[e_id][0].start, e_id))
        # return the free intervals
        return ans
