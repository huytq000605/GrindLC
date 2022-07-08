func minCost(houses []int, cost [][]int, m int, n int, target int) int {
    var dfs func(int, int, int) int
    dp := make([][][]int, len(houses))
    for i := 0; i < len(houses); i++ {
        dp[i] = make([][]int, target + 1)
        for j := 0; j < target + 1; j++ {
            dp[i][j] = make([]int, n + 1)
            for k := 0; k < n + 1; k++ {
                dp[i][j][k] = -1
            }
        }
    }
    dfs = func(idx, groups, prev int) int {
        if groups > target {
            return math.MaxInt32
        }
        if idx >= len(houses) {
            if groups == target {
                return 0
            } else {
                return math.MaxInt32
            }
        }

        if dp[idx][groups][prev] != -1 {
            return dp[idx][groups][prev]
        }

        if houses[idx] != 0 {
            new_groups := groups
            if houses[idx] != prev {
                new_groups = groups + 1
                if new_groups > target {
                    return math.MaxInt32
                }
            }
            res := dfs(idx + 1, new_groups, houses[idx])
            dp[idx][groups][prev] = res
            return res
        } else {
            result := math.MaxInt32
            for i, price := range cost[idx] {
                color := i + 1
                new_groups := groups
                if color != prev {
                    new_groups += 1
                }
                res := price + dfs(idx + 1, new_groups, color)
                if res < result {
                    result = res
                }
            }
            dp[idx][groups][prev] = result
            return result
        }
    }

    result := dfs(0, 0, 0)
    if result >= math.MaxInt32 {
        return -1
    }
    return result
}

