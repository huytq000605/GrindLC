func minOperations(nums []int, x int) int {
    n := len(nums)
    result := n+1
    seen_prefix := make(map[int]int)
    seen_prefix[0] = 0
    
    prefix := 0
    for i, num := range nums {
        prefix += num
        if prefix == x {
            result = min(result, i + 1)
        }
        seen_prefix[prefix] = i + 1
    }
    
    suffix := 0
    for i := n - 1; i >= 0; i-- {
        suffix += nums[i]
        if times, ok := seen_prefix[x - suffix]; ok {
            result = min(result, n - i + times)
        }
    }
    if result > n {
        return -1
    }
    return result
}

func min(a, b int) int {
    if a > b {
        return b
    } else {
        return a
    }
}
