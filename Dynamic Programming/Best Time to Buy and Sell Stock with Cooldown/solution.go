package main

func maxProfit(prices []int) int {
	dp := make([][][]int, len(prices))
	for i := range dp {
		dp[i] = make([][]int, 2)
		for j := range dp[i] {
			dp[i][j] = make([]int, 2)
		}
	}
	return helper(prices, 0, 0, 0, dp)
}

func helper(prices []int, index int, didBuy int, cooldown int, dp [][][]int) int {
	if index == len(prices) {
		return 0
	}
	if dp[index][didBuy][cooldown] != 0 {
		return dp[index][didBuy][cooldown]
	}
	if didBuy == 0 {
		if cooldown == 1 {
			dp[index][didBuy][cooldown] = helper(prices, index+1, 0, 0, dp)
		} else {
			buyThis := -prices[index] + helper(prices, index+1, 1, 0, dp)
			passThis := helper(prices, index+1, 0, 0, dp)
			if buyThis > passThis {
				dp[index][didBuy][cooldown] = buyThis
			} else {
				dp[index][didBuy][cooldown] = passThis
			}
		}
	} else {
		sellThis := prices[index] + helper(prices, index+1, 0, 1, dp)
		passThis := helper(prices, index+1, 1, 0, dp)
		if sellThis > passThis {
			dp[index][didBuy][cooldown] = sellThis
		} else {
			dp[index][didBuy][cooldown] = passThis
		}
	}
	return dp[index][didBuy][cooldown]

}
