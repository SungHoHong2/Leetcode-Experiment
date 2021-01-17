class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

class Solution:
    def getNonConflicting(self, jobs, n):
        # search the job that ends earlier than the current job
        for i in reversed(range(n)):
            # return the index of the nonconflict job if found
            if jobs[i].finish <= jobs[n].start:
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
        jobs.sort(key=lambda x:x.finish)
        # set a table that records the profit of each jobs according to finish time
        dp = [0 for _ in jobs]
        # record the profit that finishes the earliest
        dp[0] = jobs[0].profit
        # iterate all the jobs
        for i in range(len(jobs)):
            # get the non-conflicting job
            j = self.getNonConflicting(jobs, i)
            # update the dp table by choosing to add current job or skip it
            dp[i] = max(jobs[i].profit + dp[j], dp[i-1])
        # return the highest profit of non-conflicting jobs
        return dp[len(jobs)-1]