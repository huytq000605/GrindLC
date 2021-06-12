package main

import "math/rand"

type Solution struct {
	original []int
}

func Constructor(nums []int) Solution {
	return Solution{
		original: nums,
	}
}

/** Resets the array to its original configuration and return it. */
func (this *Solution) Reset() []int {
	return this.original
}

/** Returns a random shuffling of the array. */
func (this *Solution) Shuffle() []int {
	result := make([]int, len(this.original))
	for i := 0; i < len(result); i++ {
		result[i] = this.original[i]
	}
	for i := 0; i < len(this.original); i++ {
		random := rand.Intn(len(this.original))
		result[i], result[random] = result[random], result[i]
	}
	return result
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.Reset();
 * param_2 := obj.Shuffle();
 */
