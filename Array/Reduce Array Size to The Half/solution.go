func minSetSize(arr []int) int {
    n := len(arr)
    counter := make(map[int]int)
    for _, num := range arr {
        if _, ok := counter[num]; !ok {
            counter[num] = 0
        }
        counter[num] += 1
    }
    
    freq_counter := make(map[int]int)
    for _, freq := range counter {
        if _, ok := freq_counter[freq]; !ok {
            freq_counter[freq] = 0
        }
        freq_counter[freq] += 1
    }
    
    result := 0
    half := n / 2
    freq := n
    removed := 0
    for removed < half {
        for {
            if count, ok := freq_counter[freq]; !ok || count == 0 {
                freq -= 1
            } else {
                break
            }
        }
        result += 1
        removed += freq
        freq_counter[freq] -= 1
    }
    return result
}
