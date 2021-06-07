package main

type divide map[string]float64

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	equationMap := make(map[string]divide)
	/* Make a map have structure like
	Map {
		a : Map {
			b: 2
			c: 3
		},
		b: Map {
			a: 0.5
		}
		c: Map {
			a: 0.33
		}
	}
	*/
	for idx, equation := range equations {
		if _, ok := equationMap[equation[0]]; !ok {
			equationMap[equation[0]] = make(divide)
		}
		if _, ok := equationMap[equation[1]]; !ok {
			equationMap[equation[1]] = make(divide)
		}
		equationMap[equation[0]][equation[1]] = values[idx]
		equationMap[equation[1]][equation[0]] = 1 / values[idx]
	}
	result := make([]float64, len(queries))
	for idx, query := range queries {
		seen := make(map[string]bool)
		result[idx] = dfs(equationMap, query[0], query[1], seen)
	}
	return result
}

func dfs(equationMap map[string]divide, divisor string, dividend string, seen map[string]bool) float64 {
	if _, ok := seen[divisor]; ok {
		return -1
	}
	seen[divisor] = true
	if _, ok := equationMap[divisor]; !ok {
		return -1
	}

	if dividend == divisor {
		return 1
	}

	if result, ok := equationMap[divisor][dividend]; ok {
		return result
	}

	for newDivisor, middleValue := range equationMap[divisor] {
		res := dfs(equationMap, newDivisor, dividend, seen)
		if res != -1 {
			return middleValue * res
		}
	}
	return -1
}
