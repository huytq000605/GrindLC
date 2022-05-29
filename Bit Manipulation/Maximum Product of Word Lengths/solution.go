func maxProduct(words []string) int {
    masks := make(map[int]int)
    n := len(words)
    result := 0
    for i := 0; i < n; i++ {
        mask := 0
        for _, c := range words[i] {
            mask |= (1 << (c - 'a'))
        }
        masks[i] = mask
        for j := 0; j < i; j++ {
            if masks[i] & masks[j] == 0 {
                product := len(words[i]) * len(words[j])
                if product > result {
                    result = product
                }
            }
        }
    }
    return result
}
