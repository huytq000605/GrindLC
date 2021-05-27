package main

import (
	"sort"
)

func rangeSum(nums []int, n int, left int, right int) int {
	arr := []int{}
	result := 0
	for i := 0; i < n; i++ {
		arr = append(arr, nums[i])      // add to the arr nums[i]
		helper(&nums, i, nums[i], &arr) // helper function add to arr all the sum of [num] ( > 1 ) numbers start by index i
	}
	sort.Ints(arr)
	for i := left - 1; i < right; i++ {
		result += arr[i]
	}
	return result % 1000000007

}

func helper(nums *[]int, idx int, currentSum int, arr *[]int) {
	for i := idx + 1; i < len(*nums); i++ {
		currentSum = currentSum + (*nums)[i]
		*arr = append(*arr, currentSum)
	}
}
