package main

import "sort"

/*
We use recursion to generate all the number have sequential digits
*/

func sequentialDigits(low int, high int) []int {
    arr := make([]int, 0)
    result := make([]int, 0)
    for i := 1; i <= 9; i++ {
        generate(8, i, &arr)
    }
    for _, num := range arr {
        if (num >= low && num <= high) {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
    
}

func generate(remain int, current int, result *[]int) {
    if current > 10 {
        *result = append(*result, current)
    }
    lastNum := current % 10;
    if lastNum == 9 {
        return
    }
    generate(remain - 1, current*10 + lastNum+1, result)
}