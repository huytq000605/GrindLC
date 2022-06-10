package main

func numSubarrayProductLessThanK(nums []int, k int) int {
    product := 1
    result := 0
    start := 0
    for i := 0; i < len(nums); i++ {
        product *= nums[i]
        for start <= i && product >= k {
            product /= nums[start]
            start += 1
        }
        result += (i - start + 1)
    }
    return result
}
