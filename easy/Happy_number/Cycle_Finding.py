# Instead of keeping track of just one value in the chain,
# we keep track of 2, called the slow runner and the fast runner.
# At each step of the algorithm, the slow runner goes forward by 1 number in the chain,
# and the fast runner goes forward by 2 numbers (nested calls to the getNext(n) function).


# If n is a happy number, i.e. there is no cycle, then the fast runner will eventually get to 1 before the slow runner.

# If n is not a happy number, then eventually the fast runner and the slow runner will be on the same number.


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)

        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1