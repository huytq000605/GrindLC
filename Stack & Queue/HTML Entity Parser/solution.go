func entityParser(text string) string {
	dict := make(map[string]string)
	dict["&quot;"] = `"`
	dict["&apos;"] = `'`
	dict["&amp;"] = `&`
	dict["&gt;"] = `>`
	dict["&lt;"] = `<`
	dict["&frasl;"] = `/`

	result := text
	stack := []int{}
	for i := 0; i < len(result); i++ {
		if string(result[i]) == "&" {
			stack = append(stack, i)
		}
		if string(result[i]) == ";" {
			if len(stack) == 0 {
				continue
			}
			pop := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			str := result[pop : i+1]
			if replace, ok := dict[str]; ok {
				result = result[:pop] + replace + result[i+1:]
				i = i - len(str) + 1
			}
		}
	}
	return result
}