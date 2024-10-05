class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # dp1[i] = score when previous column has i blacks, including its contribution
        # dp2[i] = score when previous column has i blacks, excluding its contribution
        # i = number of blacks of current column
        # j = number of blacks of previous column
        # prev_val = values from previous column with j blacks and i blacks
        # cur_val = values from current column with j blacks and i blacks
        # ndp1[i] = max(ndp1[i], dp1[j] + prev_val, dp2[j])
        # ndp2[i] = max(ndp2[i], cur_val + dp2[j], cur_val + dp1[j] + prev_val)
        dp1 = [0 for _ in range(n + 1)]
        dp2 = [0 for _ in range(n + 1)]    
        for col in range(1, n):
            ndp1 = [0 for _ in range(n + 1)]
            ndp2 = [0 for _ in range(n + 1)]
            for prev_black in range(n+1):
                # for each prev_black
                # we could calculate cur_val already
                # if cur_back touches the white, we just deduct later
                prev_val = 0
                cur_val = 0
                for row in range(prev_black):
                    cur_val += grid[row][col]
                for cur_black in range(n+1):
                    if cur_black and cur_black <= prev_black:
                        cur_val -= grid[cur_black-1][col]
                    if cur_black > prev_black:
                        prev_val += grid[cur_black-1][col-1]
                    i = cur_black
                    j = prev_black
                    ndp1[i] = max(ndp1[i], dp1[j] + prev_val, dp2[j])
                    ndp2[i] = max(ndp2[i], cur_val + dp2[j], cur_val + dp1[j] + prev_val)
            dp1 = ndp1
            dp2 = ndp2
        return max(dp2)
