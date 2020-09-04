class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            # if the array length is 2*n
            if len(A) == 2*n:
                # check the validity of the parenthesis
                if valid(A):
                    # add the answer to the list
                    ans.append("".join(A))
            # if the array length is not yet full
            else:
                # append opening parenthesis
                A.append('(')
                # create all cases that starts with opening parenthesis
                generate(A)
                # return back before generating the cases
                A.pop()
                # add the closing
                A.append(')')
                # generate all the cases that starts with closing
                generate(A)
                # return back before generating the cases
                A.pop()
        def valid(A):
            # set the integer for balance
            bal = 0
            # iterate the array
            for c in A:
                # if the character is the opening
                if c == '(':
                    # increase the balance
                    bal += 1
                # if the character is closing
                else:
                    # decrease the balance
                    bal -= 1
                # if there are more closing than the opening
                if bal < 0:
                    # return false
                    return False
            # return true if the opening and closing are equal
            return bal == 0
        # set up the return array
        ans = list()
        # run the generate function
        generate()
        # return the array
        return ans