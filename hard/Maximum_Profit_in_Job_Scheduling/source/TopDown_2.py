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

    def sortScheduling(self, jobs, j):
        if j == -1:
            return 0

        if j == 0:
            return jobs[j].profit

        if not self.M[j]:
            self.M[j] = max(jobs[j].profit + self.sortScheduling(jobs, self.P[j]), self.sortScheduling(jobs, j - 1))

        return self.M[j]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list()
        for i in range(len(profit)):
            jobs.append(Job(startTime[i], endTime[i], profit[i]))

        jobs.sort(key=lambda x: x.finish)

        self.M = [0 for i in range(len(profit))]

        self.P = [self.getNonConflict(jobs, i) for i in range(len(profit))]

        return self.sortScheduling(jobs, len(profit) - 1)
