class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit


class Solution:

    def getNonConflict(self, jobs, n):
        for i in reversed(range(n)):
            if jobs[i].finish <= jobs[n].start:
                return i
        return -1

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list()
        for i in range(len(profit)):
            jobs.append(Job(startTime[i], endTime[i], profit[i]))

        jobs.sort(key=lambda x: x.finish)

        M = [0 for i in range(len(profit))]
        P = [self.getNonConflict(jobs, i) for i in range(len(profit))]
        M[0] = jobs[0].profit

        for i in range(1, len(jobs)):
            profit = jobs[i].profit
            M[i] = max(jobs[i].profit + (M[P[i]] if P[i] != -1 else 0), M[i - 1])

        return M[len(jobs) - 1]