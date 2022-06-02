package main

import "sort"

func getMaximumConsecutive(coins []int) int {
    sort.Ints(coins)
    sum := 0
    for _, coin := range coins {
        if coin > sum + 1 {
            break
        }
        sum += coin
    }
    return sum + 1
}
