### Maximum Profit in Job Scheduling

**Top-Down**
- Concept
    - Sort the jobs according to the finish time 
    - Update the dp table that tracks the maximum profit for each jobs 
        - `dp[i] = max(dp[compatible]+job[i], dp[i-1])`
            - `compatible`: job that can run right before `i` 
            - `dp[i-1]`: the highest profit possible without considering the current job 
            - `job[i]`: the profit of the current job
- [Source code](source/TopDown.py)
- [Source code(Textbook)](source/TopDown_2.py)

```python
class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

class Solution:
    def getNonConflicting(self, jobs, n):
        # search the job that ends earlier than the current job
            # return the index of the latest job that does not conflict with the current job
        # return -1 if every job is conflicting
        pass

    def sortScheduling(self, jobs, j):
        # return 0 if the recursion requests for incompatible jobs
        # return the current profit if the recursive tree reached the leaf
        # if the result of the current job is not recorded
            # find the compatible job
            # record the maximum possible profit for the current job
        # return the maximum possible profit for the current job
        pass

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # initialize a list to store jobs
        # append all the jobs (start, finish, profit)
        # sort the jobs by finish time
        # initialize a map that records the maximum profit for each jobs
        # run the recursvie tree from top to bottom
        pass 
```

**Bottom-Up**
- [Source code](source/BottomUp.py)
- [Source code(Textbook)](source/BottomUp_2.py)

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
