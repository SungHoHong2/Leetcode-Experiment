def minimum(num, k):
    numStack = []
    for digit in num:
        while k and numStack and numStack[-1] > digit:
            numStack.pop()
            k -= 1
        numStack.append(digit)
    finalStack = numStack[:-k] if k else numStack

    # trip the leading zeros
    return "".join(finalStack).lstrip('0') or "0"


def maximim(num, k):
    numStack = []
    for digit in num:
        while k and numStack and numStack[-1] < digit:
            numStack.pop()
            k -= 1

        numStack.append(digit)

    # - Trunk the remaining K digits at the end
    # - in the case k==0: return the entire list
    finalStack = numStack[:-k] if k else numStack

    # trip the leading zeros
    return "".join(finalStack).lstrip('0') or "0"


def helper(num, k):
    if num < 0:
        num = - num
        return - int(minimum(str(num), k))
    else:
        return int(maximim(str(num), k))
