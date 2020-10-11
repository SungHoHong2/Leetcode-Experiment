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

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # initialize a list to store jobs (start, finish, profit)
        jobs = list()
        # append all the jobs
        for i in range(len(profit)):
            jobs.append(Job(startTime[i], endTime[i], profit[i]))
        # sort the jobs by finish time
        jobs.sort(key=lambda x: x.finish)
        # set a table that records the profit of each jobs according to finish time
        maxProfit = [0 for i in range(len(jobs))]
        # record the profit that finishes the earliest
        maxProfit[0] = jobs[0].profit
        # iterate all the jobs
        for i in range(1, len(jobs)):
            # get the nonconflicting job
            j = self.getNonConflicting(jobs, i)
            # record the profit of the current job
            profit = jobs[i].profit
            if j != -1:
                # accumulate the profit of the nonconflicting job
                profit += maxProfit[j]
            # find the biggest profit between the new profit or profit that does apply the current job
            maxProfit[i] = max(profit, maxProfit[i - 1])
        # return the record of the final job
        return maxProfit[len(jobs) - 1]