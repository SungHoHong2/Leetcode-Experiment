class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        # iterate until leaf (tx,ty) reaches or exceeds the root (sx,sy)
        while tx >= sx and ty >= sy:
            # return true if the leaf meets the root
            if sx == tx and sy == ty: return True
            # subtract y from x if x is bigger than y
            if tx > ty:
                tx -= ty
            # subtract x from y if y is bigger than x
            else:
                ty -= tx
        # return false the leaf exceeds the root
        return False