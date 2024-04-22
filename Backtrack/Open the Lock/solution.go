package main

type lock struct {
	str   string
	level int
}

func openLock(deadends []string, target string) int {
	dead := make(map[string]bool)
	for _, deadend := range deadends {
		dead[deadend] = true
	}
	seen := make(map[string]bool)
	queue := []lock{{"0000", 0}}
	for len(queue) > 0 {
		current := queue[0]
		if current.str == target {
			return current.level
		}
		queue = queue[1:]
		if _, ok := dead[current.str]; ok {
			continue
		}
		if _, ok := seen[current.str]; ok {
			continue
		}
		seen[current.str] = true
		for i := 0; i < 4; i++ {
			str := plus(current.str, i)
			level := current.level + 1
			queue = append(queue, lock{str, level})
		}
		for i := 0; i < 4; i++ {
			str := sub(current.str, i)
			level := current.level + 1
			queue = append(queue, lock{str, level})
		}
	}
	return -1
}

func plus(str string, pos int) string {
	if str[pos] != 57 { // ASCII 57 is 9
		return str[0:pos] + string(str[pos]+1) + str[pos+1:]
	} else {
		return str[0:pos] + string(48) + str[pos+1:]
	}

}

func sub(str string, pos int) string {
	if str[pos] != 48 { // ASCII 48 is 0
		return str[0:pos] + string(str[pos]-1) + str[pos+1:]
	} else {
		return str[0:pos] + string(57) + str[pos+1:]
	}
}
