### Burst Balloons
**Top Down**
- [Concepts](images/)
    - Define a function dp to return the maximum number of coins obtainable on the open interval (left, right).
    - Base case 
        - No integers on our interval `(left + 1 == right)`
        - There are no more balloons that can be added.
    - Best score 
        - `nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right)`
        
- [Source code](source/)
- [Reference #1]()

**Bottom Up**
- [Concepts](images/)
- [Source code](source/)
- [Reference #1]()

