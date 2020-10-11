class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

class Solution:
    def getNonConflicting(self, jobs, n):
        # search the job that ends earlier than the current job
        for i in reversed(range(n)):
            # find the job that does not conflict with the current job
            if jobs[i].finish <= jobs[n].start:
                # return the index
                return i
        # if every job is conflicting return -1
        return -1

    def sortScheduling(self, jobs, j):
        # if the job is incompatible
        if j == -1:
            # return zero profit
            return 0
        # if the recursive tree reached the leaf
        if j == 0:
            # return the current profit
            return jobs[j].profit
        # if the result of the current job is not recorded
        if not self.M[j]:
            # find the compatible job
            compatible = self.getNonConflicting(jobs, j)
            # record the maximum possible profit for the current job
            self.M[j] = max(jobs[j].profit + self.sortScheduling(jobs, compatible), self.sortScheduling(jobs, j - 1))
        # return the maximum possible profit for the current job
        return self.M[j]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # initialize a list to store jobs (start, finish, profit)
        jobs = list()
        # append all the jobs
        for i in range(len(profit)):
            jobs.append(Job(startTime[i], endTime[i], profit[i]))
        # sort the jobs by finish time
        jobs.sort(key=lambda x: x.finish)
        # initialize a map that records the maximum profit for each jobs
        self.M = dict()
        for j in range(len(profit)):
            self.M[j] = 0
        # run the recursvie tree from top to bottom
        return self.sortScheduling(jobs, len(jobs) - 1)