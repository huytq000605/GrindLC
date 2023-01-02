class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:
            return False
        while tx > sx and ty > sy:
            # To go to the previous state, we must decrease the bigger tx or ty
            # If we decrease the smaller, that means tx or ty will be negative
            if tx > ty:
                # tx = previous tx + k*ty
                tx %= ty
            else:
                # ty = previous ty + k*tx
                ty %= tx
        return (tx == sx and (ty - sy) % tx == 0) or \
               (ty == sy and (tx - sx) % ty == 0)