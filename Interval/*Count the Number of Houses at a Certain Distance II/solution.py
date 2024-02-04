class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y = y, x
        # length of left, cycle, right
        n1, nc, n2 = x-1, y-x+1, n-y
        result = [0 for _ in range(n+1)]

        def line(n):
            nonlocal result
            # for each point from 1 -> n
            # increase 1 from mn to mx
            for i in range(1, n+1):
                if i+1 > n: continue
                mn = 1
                mx = n-i
                result[mn] += 1
                if mx + 1 < len(result):
                    result[mx+1] -= 1
            
        def cycle(n):
            nonlocal result
            # each point will contribute 1 pair with distance from 1 to n//2 pairs
            for i in range(n):
                mn = 1
                mx = n//2
                result[mn] += 1
                result[mx+1] -= 1
            
            # in the case where length of cycle is even
            # the number of pairs with distance = n//2 is actually halved because there will be duplicated
            if n % 2 == 0:
                result[n//2] -= n//2
                result[n//2+1] += n//2

        def line_line(n1, n2):
            nonlocal result
            # i is distance from point on n1 to x
            for i in range(1, n1+1):
                mn = i + 1 + 1 # i + (x->y) + y->p2
                mx = i + 1 + n2 # i + (x->y) + max(y->p2)
                result[mn] += 1
                result[mx+1] -= 1
        
        def line_cycle(n, c):
            if n == 0: return
            nonlocal result
            # Let's call X is point where circle starts
            # i is distance from p1 to X
            # For each distance from (1 to C//2), there are 2 points in circle that X can go to
            for i in range(1, n+1):
                mn = i+1
                mx = i+c//2
                result[mn] += 2
                result[mx+1] -= 2

                # Theres is only 1 way to go to X from each point
                result[i] += 1
                result[i+1] -= 1
            # The only special situation is when C is even
            # There is only 1 point that S = C//2 when going from X
            if c % 2 == 0:
                for i in range(1, n+1):
                    result[i+c//2] -= 1
                    result[i+c//2+1] += 1
            
        # If circle length <= 2, solve it as there is no circle
        if nc <= 2:
            line(n1 + nc + n2)
            for i in range(1, n+1):
                result[i] += result[i-1]
            
            return [v*2 for v in result[1:]]
        line(n1)
        line(n2)
        line_cycle(n1, nc)
        line_cycle(n2, nc)
        line_line(n1, n2)
        cycle(nc)

        for i in range(1, n):
            result[i] += result[i-1]
        return [v*2 for v in result[1:]]
