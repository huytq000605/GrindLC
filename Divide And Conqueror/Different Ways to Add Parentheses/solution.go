package main

import (
	"strconv"
	"strings"
)

/*
Whenever we found an expression, we can split it into 2 parts to caculate all result of it, the base case is when we get no expression in input string => so it will only have a number, Atoi it then return slice contains only that number
*/

func diffWaysToCompute(expression string) []int {
	result := make([]int, 0)
	if strings.IndexByte(expression, 42) == -1 && strings.IndexByte(expression, 43) == -1 && strings.IndexByte(expression, 45) == -1 {
		res, _ := strconv.Atoi(expression)
		return []int{res}
	}
	for i := range expression {
		if expression[i] == 42 || expression[i] == 43 || expression[i] == 45 {
			exp := expression[i]
			exp1 := diffWaysToCompute(expression[:i])
			exp2 := diffWaysToCompute(expression[i+1:])
			for _, i1 := range exp1 {
				for _, i2 := range exp2 {
					switch exp {
					case 43: // +
						result = append(result, i1+i2)
					case 45: // -
						result = append(result, i1-i2)
					case 42: // *
						result = append(result, i1*i2)
					}
				}
			}
		}

	}
	return result
}

// Place the parentheses in string
// Write a function to take a input string then compute by stack parenthese
