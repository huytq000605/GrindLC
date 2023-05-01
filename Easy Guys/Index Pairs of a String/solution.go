func indexPairs(text string, words []string) [][]int {
    n := len(text)
    result := make([][]int, 0)
    for _, word := range words {
        m := len(word)
        for i := 0; i <= n - m; i++ {
            if text[i:i+m] == word {
                result = append(result, []int{i, i+m-1})
            }
        }
    }
    sort.Slice(result, func(i, j int) bool {
        if result[i][0] < result[j][0] {
            return true
        }
        if result[i][0] > result[j][0] {
            return false
        }
        if result[i][1] < result[j][1] {
            return true
        }
        return false
    })
    return result
}
