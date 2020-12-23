class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # set a list to collect free intervals
        ans = []
        # create a heap with element [start time, employee id, 'th job]
        pq = [(emp[0].start, ei, 0) for ei, emp in enumerate(schedule)]
        heapq.heapify(pq)
        # get the earliest start time
        anchor = min(iv.start for emp in schedule for iv in emp)
        # loop the heap until depleted
        while pq:
            # get the time, employee id, 'th job from the heap
            t, e_id, e_jx = heapq.heappop(pq)
            # if the time does not overlap
            if anchor < t:
                # append the interval to the return list
                ans.append(Interval(anchor, t))
            # updating the finishing time
            anchor = max(anchor, schedule[e_id][e_jx].end)
            # if the current employee has a future schedule
            if e_jx + 1 < len(schedule[e_id]):
                # push the next schedule to the heap
                heapq.heappush(pq, (schedule[e_id][e_jx+1].start, e_id, e_jx+1))
        # return the free intervals
        return ans