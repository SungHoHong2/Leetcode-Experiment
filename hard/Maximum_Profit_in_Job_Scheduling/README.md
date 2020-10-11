### Maximum Profit in Job Scheduling

**Top-Down**
- [Source code](source/TopDown.py)
```python
class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

class Solution:
    def getNonConflicting(self, jobs, n):
        # search the job that ends earlier than the current job
            # find the job that does not conflict with the current job
                # return the index
        # if every job is conflicting return -1
        pass

    def sortScheduling(self, jobs, j):
        # if the job is incompatible
            # return zero profit
        # if the recursive tree reached the leaf
            # return the current profit
        # if the result of the current job is not recorded
            # find the compatible job
            # record the maximum possible profit for the current job
        # return the maximum possible profit for the current job
        pass

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # initialize a list to store jobs (start, finish, profit)
        # append all the jobs
        # sort the jobs by finish time
        # initialize a map that records the maximum profit for each jobs
        # run the recursvie tree from top to bottom
        pass 
```

**Bottom-Up**
- [Source code](source/BottomUp.py)
```python
class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

class Solution:
    def getNonConflicting(self, jobs, n):
        # search the job that ends earlier than the current job
            # find the job that does not conflict with the current job
                # return the index
        # if every job is conflicting return -1
        pass

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # initialize a list to store jobs (start, finish, profit)
        # append all the jobs
        # sort the jobs by finish time
        # set a table that records the profit of each jobs according to finish time
        # record the profit that finishes the earliest
        # iterate all the jobs
            # get the nonconflicting job
            # record the profit of the current job
                # accumulate the profit of the nonconflicting job
            # find the biggest profit between the new profit or profit that does apply the current job
        # return the record of the final job
        pass
```
