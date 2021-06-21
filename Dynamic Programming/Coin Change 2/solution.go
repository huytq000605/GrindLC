package main

import "fmt"

func change(amount int, coins []int) int {
	cache := make(map[string]int)
	return helper(amount, coins, 0, cache)
}

func helper(amount int, coins []int, index int, cache map[string]int) int {
	key := fmt.Sprintf("%v-%v", amount, index)
	if _, ok := cache[key]; ok {
		return cache[key]
	}
	if amount == 0 {
		return 1
	}
	if amount < 0 || index == len(coins) {
		return 0
	}
	cache[key] = helper(amount-coins[index], coins, index, cache) + helper(amount, coins, index+1, cache)
	return cache[key]
}
