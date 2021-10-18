DFS in "Brace" questions
modify the current string cause open brace in stack doesn't change start


``` typescript
function(originalString: string) {
	let dfs = (index: number, str: string, stack: number[]) {
		for(let i = index; i < str.length; i++) {
			if(str[i] === "(") stack.push(i)
			if(....)
		}
		// smt happens
		str = str.slice(0, change) + smt + str.slice(afterChange)
		dfs(index + smt.length, str, [...stack]) // The index of open brace still true in stack
	}

}

```