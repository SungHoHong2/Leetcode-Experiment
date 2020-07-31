class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # set the return array
        ans = []
        # set a hashmap to store all fizzbuzz mappings
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}
        # iterate the numbers
        for num in range(1,n+1):
            # set a temp string
            num_ans_str = ""
            # iterate the available keys in the hashmap
            for key in fizz_buzz_dict.keys():
                # If the num is divisible by key,
                if num % key == 0:
                    # then add the corresponding string mapping to current num_ans_str
                    num_ans_str += fizz_buzz_dict[key]
            # if there is no divisible nums
            if not num_ans_str:
                # add the num
                num_ans_str = str(num)
            # Append the current answer str to the ans list
            ans.append(num_ans_str)
        # return the array
        return ans