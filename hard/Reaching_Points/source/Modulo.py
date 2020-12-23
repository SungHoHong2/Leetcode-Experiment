class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        # iterate until leaf (tx,ty) reaches or exceeds the root (sx,sy)
        while tx >= sx and ty >= sy:
            # stop the search if tx and ty are equal
            if tx == ty:
                break
            # if tx is larger than ty
            elif tx > ty:
                # if ty did not reached the root
                if ty > sy:
                    # subtract tx to the very limit
                    tx %= ty
                # if ty reached the root
                else:
                    # check whether the ty can reduce tx to sx
                    return (tx - sx) % ty == 0
            # same operation
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0
        # return true if tx and ty reached the root
        return tx == sx and ty == sy