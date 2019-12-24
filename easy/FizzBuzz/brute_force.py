class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        rtnArray = []

        for i in range(1, n + 1):

            if i != 0 and i % 3 == 0:
                rtnArray.append("Fizz")
            elif i != 0 and i % 5 == 0:
                rtnArray.append("Buzz")
            else:
                rtnArray.append(str(i))

            if i != 0 and i % 3 == 0 and i % 5 == 0:
                rtnArray.pop()
                rtnArray.append("FizzBuzz")

        return rtnArray
