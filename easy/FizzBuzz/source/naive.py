class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # set the return array
        ans = []
        # iterate through the nums
        for num in range(1, n + 1):
            # check whether the current number is divisible by 3
            divisible_by_3 = (num % 3 == 0)
            # check whether the current number is divisible by 5
            divisible_by_5 = (num % 5 == 0)
            # Divides by both 3 and 5, add FizzBuzz
            if divisible_by_3 and divisible_by_5:
                ans.append("FizzBuzz")
            # Divides by 3, add Fizz
            elif divisible_by_3:
                ans.append("Fizz")
            # Divides by 5, add Buzz
            elif divisible_by_5:
                ans.append("Buzz")
            # Not divisible by 3 or 5, add the number
            else:
                ans.append(str(num))
        # return array
        return ans